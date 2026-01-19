from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, create_engine, Session, Relationship

class Problem(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    
    solutions: List["Solution"] = Relationship(back_populates="problem")
    memos: List["Memo"] = Relationship(back_populates="problem")

class Solution(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    problem_id: int = Field(foreign_key="problem.id")
    language: str
    filepath: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    problem: Problem = Relationship(back_populates="solutions")

class Memo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    problem_id: int = Field(foreign_key="problem.id")
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    problem: Problem = Relationship(back_populates="memos")

sqlite_file_name = "boj.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
