from sqlalchemy.orm import Session
from . import models, schemas


def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(
        name=student.name,
        animal=student.animal
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    for g in student.grades:
        db.add(models.Grade(
            subject=g.subject,
            score=g.score,
            student_id=db_student.id
        ))

    db.commit()
    db.refresh(db_student)
    return db_student


def get_students(db: Session):
    return db.query(models.Student).all()
