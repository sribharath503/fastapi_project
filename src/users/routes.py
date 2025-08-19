from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db import get_db
from src.users.models import User
from src.users.schemas import UserCreate, Token
from src.users.security import hash_password, verify_password
from src.users.jwt_handler import create_access_token
from src.users.auth import get_current_user, get_admin_user

user_router = APIRouter()

@user_router.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = User(username=user.username, hashed_password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    token = create_access_token({"sub": new_user.username})
    return {"access_token": token, "token_type": "bearer"}

@user_router.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}

@user_router.get("/secure-data")
def secure_data(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello {current_user.username}, you're authenticated!"}

@user_router.get("/admin-only")
def admin_data(admin_user: User = Depends(get_admin_user)):
    return {"message": f"Welcome Admin {admin_user.username}"}