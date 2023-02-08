import fastapi
from fastapi import Path
from pydantic import BaseModel
from typing import Optional, List

router = fastapi.APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@router.get('/users', response_model = List[User])
async def get_users():
    return users 

@router.get('/users/{id}')
async def get_user(id):
    return users[id]

@router.post('/users')
async def post_users(user: User):
    users.append(user)
    return "Success"