from fastapi import FastAPI
from api import users, courses, sections
from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="FastAPI LMS",
    description="Basic CRUD for LMS systems",
    version="0.0.1",
    contact={
        "name": "Raghav",
        "url": "https://github.com/Raghav-Dhir"
    }
)

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)