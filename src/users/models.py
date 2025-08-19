from src.db import Base
from sqlalchemy import Integer,Column,String


class User(Base):
    __tablename__="users"

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(50),unique=True,index=True)
    hashed_password = Column(String(300))
    role = Column(String(100),default="admin")