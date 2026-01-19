import os
import time
from playwright.sync_api import sync_playwright
from sqlmodel import Session, select
from database import create_db_and_tables, engine, Problem, Solution, Memo

USER_ID = "singun11"
BASE_URL = "https://www.acmicpc.net"
SOURCE_DIR = "data/source"

def get_extension(lang_text: str) -> str:
    lang_text = lang_text.lower().strip()
    if "python" in lang_text or "pypy" in lang_text: return "py"
    if "c++" in lang_text: return "cpp"
    if "java" in lang_text and "script" not in lang_text: return "java" # Avoid JavaScript matching Java
    if "node" in lang_text or "javascript" in lang_text: return "js"
    if "rust" in lang_text: return "rs"
    if "go" in lang_text: return "go"
    if "c11" in lang_text or "c99" in lang_text or lang_text == "c": return "c"
    if "kotlin" in lang_text: return "kt"
    if "ruby" in lang_text: return "rb"
    if "swift" in lang_text: return "swift"
    if "text" in lang_text: return "txt"
    return "txt"

def scrape():
    create_db_and_tables()
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # 1. Login
        print("Navigating to login page...")
        page.goto(f"{BASE_URL}/login?next=%2F")
        print("Please log in manually in the browser.")
        input("Press Enter after you have logged in...")
        
        # 2. Get Solved Problems with Title
        print(f"Fetching solved problems for {USER_ID}...")
        page.goto(f"{BASE_URL}/user/{USER_ID}")
        
        # Select all a tags with class result-ac
        # user provided example: <a href="/problem/1004" ... data-original-title="어린 왕자">1004</a>
        problem_links = page.locator("a.result-ac").all()
        print(f"Found {len(problem_links)} solved problems.")
        
        solved_problems_data = [] # List of tuples (id, title)
        
        for link in problem_links:
            try:
                # Extract ID from text or href
                pid_text = link.inner_text().strip()
                if not pid_text.isdigit(): continue
                pid = int(pid_text)
                
                # Default Title
                title = f"Problem {pid}"
                
                solved_problems_data.append((pid, title))
            except Exception as e:
                print(f"Error parsing problem link: {e}")
        
        # Sort by ID
        solved_problems_data.sort(key=lambda x: x[0])
        print(f"Parsed {len(solved_problems_data)} valid problems.")
        
        with Session(engine) as session:
            for pid, title in solved_problems_data:
                # Upsert problem
                problem = session.exec(select(Problem).where(Problem.id == pid)).first()
                if not problem:
                    problem = Problem(id=pid, title=title)
                    session.add(problem)
                    session.commit()
                    print(f"Added Problem {pid}: {title}")
                
                # Check if we already have a solution
                existing_solution = session.exec(select(Solution).where(Solution.problem_id == pid)).first()
                if existing_solution:
                   print(f"Skipping Problem {pid} (Already scraped)")
                   continue

                # 3. Fetch Solution Code
                print(f"Fetching solution for Problem {pid}...")
                status_url = f"{BASE_URL}/status?option-status-pid=on&problem_id={pid}&user_id={USER_ID}&language_id=-1&result_id=4&from_mine=1"
                page.goto(status_url)
                
                # Structure: tr -> td:nth-child(7) is Language column
                # We target the 7th column explicitly to avoid grabbing the Result column link (e.g. "100점")
                source_link = page.locator("tr td:nth-child(7) a[href^='/source/']").first
                
                if not source_link.count():
                    print(f"No source link found for Problem {pid}")
                    continue
                
                href = source_link.get_attribute("href")
                
                # Extract language from the link text as per user hint
                lang_text = source_link.inner_text().strip()
                # If link text is 'Edit' or empty, fallback to other columns? 
                # Usuaully for own submissions in 'status' view, the language name IS the link.
                
                submission_id = href.split("/")[-1]
                
                print(f"Navigating to source: {href} (Lang: {lang_text})")
                page.goto(f"{BASE_URL}{href}")
                
                # Code extraction
                code_content = ""
                if page.locator("textarea[name='source']").count() > 0:
                     code_content = page.locator("textarea[name='source']").input_value()
                else:
                    lines = page.locator(".CodeMirror-line").all_inner_texts()
                    code_content = "\n".join(lines)
                
                if not code_content:
                     if page.locator("pre.brush").count() > 0:
                         code_content = page.locator("pre.brush").inner_text()
                
                if not code_content:
                    print(f"Could not extract code for {pid}")
                    continue

                # Determine extension
                ext = get_extension(lang_text)
                
                filename = f"{pid}_{submission_id}.{ext}"
                filepath = os.path.join(SOURCE_DIR, filename)
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(code_content)
                
                solution = Solution(
                    problem_id=pid,
                    language=lang_text, # Save original language string
                    filepath=filepath
                )
                session.add(solution)
                session.commit()
                print(f"Saved solution for {pid} ({lang_text} -> .{ext})")
                
                time.sleep(1)

if __name__ == "__main__":
    scrape()
