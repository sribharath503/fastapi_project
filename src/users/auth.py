from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import session
from src.db import get_db
from src.users.jwt_handler import decode_access_token
from src.users.models import User


oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token:str=Depends(oauth2_scheme),db:session=Depends(get_db)):
    payload=decode_access_token(token)
    username:str = payload.get("sub")
    if username is None:
        raise HTTPException(status_code=401,detail="Invalid Token Payload")
    user=db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user

def get_admin_user(current_user:User = Depends(get_current_user))->User:
    if current_user.role!="admin":
        raise HTTPException(status_code=403,detail="Admin access required")
    return current_user