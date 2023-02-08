import fastapi
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from typing import List
from api.utils.user import get_user, get_user_by_email, get_users, create_user
from db.db_setup import get_db
from schemas.user import User, UserCreate

router = fastapi.APIRouter()

@router.get('/users/', response_model = List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.get('/users/{id}')
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/users/", response_model=User)
def post_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)