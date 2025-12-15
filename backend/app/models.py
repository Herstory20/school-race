from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    animal = Column(String, nullable=True)

    grades = relationship(
        "Grade",
        back_populates="student",
        cascade="all, delete-orphan"
    )


class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, nullable=False)
    score = Column(Float, nullable=False)

    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="grades")
