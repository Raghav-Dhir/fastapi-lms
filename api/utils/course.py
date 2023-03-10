from sqlalchemy.orm import Session

from schemas.course import CourseCreate
from db.models.course import Course


def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def get_courses(db: Session):
    return db.query(Course).all()

def get_course_by_title(db: Session, title: str):
    return db.query(Course).filter(Course.title == title).first()

def create_course(db: Session, course: CourseCreate):
    db_course = Course(title=course.title, description=course.description, user_id=course.user_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course