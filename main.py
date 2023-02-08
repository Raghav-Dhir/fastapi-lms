from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional, List


app = FastAPI(
    title="FastAPI LMS",
    description="Basic CRUD for LMS systems",
    version="0.0.1",
    contact={
        "name": "Raghav",
        "url": "https://github.com/Raghav-Dhir"
    }
    )

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@app.get('/users', response_model = List[User])
async def get_users():
    return users 

@app.get('/users/{id}')
async def get_user(id: int = Path(..., description="give user id for retreiving info")):
    return users[id]

@app.post('/users')
async def post_users(user: User):
    users.append(user)
    return "Success"