from pydantic import BaseModel
from typing import Optional


class BookModel(BaseModel):
    title:str
    author:str
    pages:int 
    published_year:int

class UpdateBookModel(BaseModel):
    title:str
    author:str
    pages:int
    published_year:int

class book_out(BookModel):
    id:int
    class config:
        orm_mode:True