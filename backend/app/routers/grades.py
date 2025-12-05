from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/api")

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/students", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@router.get("/students", response_model=list[schemas.Student])
def list_students(db: Session = Depends(get_db)):
    return crud.get_students(db)
