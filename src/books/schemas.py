from pydantic import BaseModel


class BookModel(BaseModel):
    id:int
    title:str
    author:str
    year:int
    genre:str

class UpdateBookModel(BaseModel):
    title:str
    author:str
    year:int
    genre:str