import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.course import Course, CourseCreate
from db.db_setup import get_db
from api.utils.course import get_course, get_courses, create_course, get_course_by_title


router = fastapi.APIRouter()


@router.get('/courses/', response_model = List[Course])
def read_courses(db: Session = Depends(get_db)):
    courses = get_courses(db)
    return courses


@router.post("/courses/", response_model=Course)
def post_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = get_course_by_title(db, title=course.title)
    if db_course:
        raise HTTPException(status_code=400, detail="title already registered")
    return create_course(db=db, course=course)


@router.get('/courses/{id}')
def read_course(id: int, db: Session = Depends(get_db)):
    db_course = get_course(db, course_id=id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return db_course


@router.patch("/courses/{id}")
async def update_course():
    return {"courses": []}


@router.delete("/courses/{id}")
async def delete_course():
    return {"courses": []}


@router.get("/courses/{id}/sections")
async def read_course_sections():
    return {"courses": []}