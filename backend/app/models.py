from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    avatar = Column(String, nullable=True)
    grades = relationship("Grade", back_populates="student", cascade="all,delete")

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    subject = Column(String)
    score = Column(Float)
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="grades")
