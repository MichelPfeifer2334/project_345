from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List, Annotated
from .models import Question, Choices
from .database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager



app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup")
    Base.metadata.create_all(bind=engine)
    # This function is called when the application starts
    yield
    print("Application shutdown")
    # This function is called when the application stops

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # List of allowed origins
    allow_credentials=True, # Allow credentials (cookies, authorization headers, etc.)
    allow_methods=["*"], # Allow all HTTP methods
    allow_headers=["*"], # Allow all HTTP headers
)


@app.post("/questions/")
async def create_question(question: QuestionBase, db: db_dependency):
    db_question = Question(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    for choice in question.choices:
        db_choice = Choices(
            choice_text=choice.choice_text,
            is_correct=choice.is_correct,
            question_id=db_question.id
        )
        db.add(db_choice)

    db.commit()
    return {"message": "Question created successfully", "question_id": db_question.id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

