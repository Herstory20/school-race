from pydantic import BaseModel
from typing import List, Optional

class GradeCreate(BaseModel):
    subject: str
    score: float

class StudentCreate(BaseModel):
    name: str
    avatar: Optional[str] = None
    grades: List[GradeCreate] = []

class Grade(BaseModel):
    id: int
    subject: str
    score: float
    class Config: orm_mode = True

class Student(BaseModel):
    id: int
    name: str
    avatar: Optional[str]
    grades: List[Grade]
    class Config: orm_mode = True
