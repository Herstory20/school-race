from pydantic import BaseModel
from typing import List, Optional


class GradeCreate(BaseModel):
    subject: str
    score: float


class Grade(BaseModel):
    id: int
    subject: str
    score: float

    class Config:
        orm_mode = True


class StudentCreate(BaseModel):
    name: str
    animal: Optional[str] = None
    grades: List[GradeCreate]


class Student(BaseModel):
    id: int
    name: str
    animal: Optional[str]
    grades: List[Grade]

    class Config:
        orm_mode = True
