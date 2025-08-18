from sqlalchemy import Column,Integer,String
from src.db import Base


class books_model(Base):
    __tablename__="Books"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(100))
    author=Column(String(100))
    pages=Column(Integer)
    published_year=Column(Integer)