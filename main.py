import os
import shutil
import time
from typing import Optional

from dotenv import load_dotenv
import httpx
from fastapi import FastAPI, Request, Depends, HTTPException, File, UploadFile, Form, status, BackgroundTasks
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from sqlmodel import Session, select, func

from database import engine, get_session, create_db_and_tables, Problem, Solution, Memo

# Load .env
load_dotenv()
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "secret")
SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key-change-me")

app = FastAPI()

# Add Session Middleware
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/data", StaticFiles(directory="data"), name="data")

templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Helper to check if user is admin from session
def is_admin(request: Request) -> bool:
    return request.session.get("user") == "admin"

# Helper for Solved.ac API
async def get_solved_ac_title(problem_id: int) -> Optional[str]:
    try:
        async with httpx.AsyncClient() as client:
            headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
            resp = await client.get(f"https://solved.ac/api/v3/problem/show?problemId={problem_id}", headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                return data.get("titleKo")
            else:
                print(f"Solved.ac API Error {problem_id}: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"Exception fetching {problem_id}: {e}")
    return None

def get_extension(lang: str) -> str:
    lang = lang.lower()
    if "python" in lang: return ".py"
    if "c++" in lang or "cpp" in lang: return ".cpp"
    if "java" in lang: return ".java"
    if "rust" in lang: return ".rs"
    if "go" in lang: return ".go"
    if "node" in lang or "javascript" in lang: return ".js"
    if "swift" in lang: return ".swift"
    if "kotlin" in lang: return ".kt"
    if "ruby" in lang: return ".rb"
    if "c" == lang: return ".c"
    return ".txt"

@app.get("/admin/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/admin/login")
async def login(request: Request, password: str = Form(...)):
    if password == ADMIN_PASSWORD:
        request.session["user"] = "admin"
        return RedirectResponse(url="/", status_code=303)
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid Password"})

@app.get("/admin/logout")
async def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse(url="/", status_code=303)

@app.get("/", response_class=HTMLResponse)
async def read_root(
    request: Request, 
    session: Session = Depends(get_session),
    page: int = 1,
    limit: int = 50,
    q: Optional[str] = None,
    lang: Optional[str] = None
):
    # Base query
    query = select(Problem)
    
    # Filter by Language
    if lang:
        query = query.join(Solution).where(Solution.language == lang).distinct()
        
    # Filter by Search (Problem ID)
    if q:
        try:
            q_id = int(q)
            query = query.where(Problem.id == q_id)
        except ValueError:
            pass # Ignore non-integer search for ID
            
    # Count total results (Simplified)
    results = session.exec(query).all()
    total_items = len(results)
    total_pages = (total_items + limit - 1) // limit
    
    # Apply Pagination
    start = (page - 1) * limit
    end = start + limit
    paginated_problems = results[start:end]
    
    # Calculate Page Range (Max 10 pages, centered)
    # e.g. if page 6, show 1..10. if page 100, show 95..104
    start_p = max(1, page - 5)
    end_p = min(total_pages, start_p + 9)
    # Adjust start if end is capped
    if end_p - start_p < 9:
        start_p = max(1, end_p - 9)
    
    page_range = range(start_p, end_p + 1)
    
    # Get all available languages for filter
    all_langs = session.exec(select(Solution.language).distinct()).all()
    all_langs = sorted([l for l in all_langs if l])

    return templates.TemplateResponse("index.html", {
        "request": request, 
        "problems": paginated_problems,
        "is_admin": is_admin(request),
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
        "page_range": list(page_range),
        "q": q,
        "lang": lang,
        "all_langs": all_langs
    })

# Helper for PrismJS class mapping
def get_prism_lang(lang: str) -> str:
    lang = lang.lower()
    if "python" in lang: return "python"
    if "c++" in lang or "cpp" in lang: return "cpp"
    if "java" in lang and "script" not in lang: return "java"
    if "node" in lang or "javascript" in lang: return "javascript"
    if "rust" in lang: return "rust"
    if "go" in lang: return "go"
    if "kotlin" in lang: return "kotlin"
    if "swift" in lang: return "swift"
    if "ruby" in lang: return "ruby"
    if "c" == lang or "c11" in lang or "c99" in lang: return "c"
    return "clike" # Fallback

@app.get("/grass", response_class=HTMLResponse)
async def view_grass(request: Request, session: Session = Depends(get_session)):
    # Fetch all solved problem, title pairs
    problems = session.exec(select(Problem)).all()
    # Create simple map: {id: title}
    solved_map = {p.id: p.title for p in problems}
    
    return templates.TemplateResponse("grass.html", {
        "request": request,
        "solved_map": solved_map,
        "is_admin": is_admin(request)
    })

@app.get("/problem/{problem_id}", response_class=HTMLResponse)
async def read_problem(problem_id: int, request: Request, session: Session = Depends(get_session)):
    problem = session.get(Problem, problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    
    solutions = problem.solutions
    memos = problem.memos
    memo_content = memos[0].content if memos else ""
    
    solution_data = []
    for sol in solutions:
        code = ""
        if os.path.exists(sol.filepath):
            with open(sol.filepath, "r", encoding="utf-8") as f:
                code = f.read()
        char_count = len(code)
        byte_count = len(code.encode('utf-8'))
        if byte_count < 1024:
            byte_str = f"{byte_count} B"
        else:
            byte_str = f"{byte_count / 1024:.1f} KB"

        solution_data.append({
            "id": sol.id,
            "language": sol.language,
            "prism_lang": get_prism_lang(sol.language),
            "code": code,
            "filepath": sol.filepath,
            "char_count": char_count,
            "byte_str": byte_str
        })

    return templates.TemplateResponse("detail.html", {
        "request": request,
        "problem": problem,
        "solutions": solution_data,
        "memo_content": memo_content,
        "is_admin": is_admin(request)
    })

@app.post("/problem/{problem_id}/memo")
async def update_memo(problem_id: int, request: Request, content: str = Form(...), session: Session = Depends(get_session)):
    if not is_admin(request):
        raise HTTPException(status_code=403, detail="Not authorized")
        
    problem = session.get(Problem, problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    
    memo = session.exec(select(Memo).where(Memo.problem_id == problem_id)).first()
    if memo:
        memo.content = content
        session.add(memo)
    else:
        memo = Memo(problem_id=problem_id, content=content)
        session.add(memo)
    
    session.commit()
    return RedirectResponse(url=f"/problem/{problem_id}", status_code=303)

@app.post("/upload")
async def upload_code(
    request: Request,
    problem_id: int = Form(...), 
    language: str = Form(...),
    code_content: str = Form(...),
    session: Session = Depends(get_session)
):
    if not is_admin(request):
        raise HTTPException(status_code=403, detail="Not authorized")
        
    problem = session.get(Problem, problem_id)
    if not problem:
        # Fetch title from Solved.ac
        title = await get_solved_ac_title(problem_id)
        if not title:
            title = f"Problem {problem_id}"
            
        problem = Problem(id=problem_id, title=title)
        session.add(problem)
        session.commit()
        session.refresh(problem)
    
    # Create file
    ext = get_extension(language)
    timestamp = int(time.time())
    filename = f"{problem_id}_manual_{timestamp}{ext}"
    save_path = f"data/source/{filename}"
    
    try:
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(code_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to write file: {str(e)}")
        
    solution = Solution(
        problem_id=problem_id,
        language=language,
        filepath=save_path
    )
    session.add(solution)
    session.commit()
    
    return RedirectResponse(url=f"/problem/{problem_id}", status_code=303)

import asyncio

@app.post("/admin/sync-titles")
async def sync_titles(request: Request, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    if not is_admin(request):
        raise HTTPException(status_code=403, detail="Not authorized")
    
    background_tasks.add_task(run_sync_titles_job)
    print("Background sync job started.")
    return RedirectResponse(url="/", status_code=303)

async def run_sync_titles_job():
    print("Starting background title sync...")
    with Session(engine) as session:
        # 1. Identify candidates
        problems = session.exec(select(Problem)).all()
        candidates = [p for p in problems if p.title == f"Problem {p.id}"]
        
        if not candidates:
            print("No titles to sync.")
            return

        print(f"Found {len(candidates)} problems to sync.")

        # 2. Async Fetch with Rate Limiting
        # Solved.ac returns 429 easily. Use sequential execution with delay.
        sem = asyncio.Semaphore(1) 
        
        async def fetch_and_update(prob):
            async with sem:
                await asyncio.sleep(1.5) # Conservative rate limit
                title = await get_solved_ac_title(prob.id)
                return prob, title
        
        # Process in chunks of 10 to commit incrementally
        chunk_size = 10
        total_synced = 0
        
        # We can't easily "chunk" the async gather if we want parallelism across all.
        # But user asked to "update query every 10".
        # Better approach: Run all tasks, but processing results or processing in batches?
        # "Is process during which 10 update queries are sent" -> User likely means "Commit every 10 items" or "Fetch 10, Save 10".
        # Let's do "Fetch 10, Save 10" to be safe and interactive in logs.
        
        for i in range(0, len(candidates), chunk_size):
            batch = candidates[i : i + chunk_size]
            tasks = [fetch_and_update(p) for p in batch]
            results = await asyncio.gather(*tasks)
            
            updates_in_batch = 0
            for prob, title in results:
                if title and prob.title != title:
                    prob.title = title
                    session.add(prob)
                    updates_in_batch += 1
            
            if updates_in_batch > 0:
                session.commit()
                total_synced += updates_in_batch
                print(f"Synced batch: {total_synced} titles updated so far...")
                
        print(f"Sync complete. Total updated: {total_synced}")

@app.post("/admin/solution/{solution_id}/delete")
async def delete_solution(solution_id: int, request: Request, session: Session = Depends(get_session)):
    if not is_admin(request):
        raise HTTPException(status_code=403, detail="Not authorized")
        
    solution = session.get(Solution, solution_id)
    if not solution:
        raise HTTPException(status_code=404, detail="Solution not found")
        
    # Delete file
    if os.path.exists(solution.filepath):
        try:
            os.remove(solution.filepath)
        except Exception as e:
            print(f"Error deleting file {solution.filepath}: {e}")
            
    # Delete from DB
    problem_id = solution.problem_id
    session.delete(solution)
    session.commit()
    
    return RedirectResponse(url=f"/problem/{problem_id}", status_code=303)

@app.post("/problem/{problem_id}/solution/{solution_id}/edit")
async def edit_solution(
    problem_id: int, 
    solution_id: int, 
    request: Request, 
    code_content: str = Form(...), 
    session: Session = Depends(get_session)
):
    if not is_admin(request):
        raise HTTPException(status_code=403, detail="Not authorized")
        
    solution = session.get(Solution, solution_id)
    if not solution:
        raise HTTPException(status_code=404, detail="Solution not found")
        
    # Security check: Ensure filepath is within data directory
    if not os.path.abspath(solution.filepath).startswith(os.path.abspath("data/source")):
        raise HTTPException(status_code=400, detail="Invalid filepath security check failed")

    # Update file
    try:
        with open(solution.filepath, "w", encoding="utf-8") as f:
            f.write(code_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to write file: {str(e)}")
        
    return RedirectResponse(url=f"/problem/{problem_id}", status_code=303)
