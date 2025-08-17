from fastapi import FastAPI,HTTPException,status
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

books = [
    {
        "id": 1,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "year": 1999,
        "genre": "Software Engineering"
    },
    {
        "id": 2,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
        "genre": "Programming"
    },
    {
        "id": 3,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "year": 2015,
        "genre": "Python"
    },
    {
        "id": 4,
        "title": "Design Patterns",
        "author": "Erich Gamma",
        "year": 1994,
        "genre": "Software Design"
    },
    {
        "id": 5,
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "year": 2009,
        "genre": "Algorithms"
    }
]

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

@app.get("/get_all_books")
async def get_all_books():
    return books

@app.get("/get_book/{book_id}")
async def get_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="book not found")

@app.post("/create_book")
async def create_book(book_data:BookModel):
    new_book=book_data.model_dump()
    books.append(new_book)
    return new_book


@app.patch("/update_book/{book_id}")
async def update_book(book_id:int,update_book_data:UpdateBookModel):
    for book in books:
        if book["id"] == book_id:
            book["title"]=update_book_data.title
            book["author"]=update_book_data.author
            book["year"]=update_book_data.year
            book["genre"]=update_book_data.genre

            return book
    
    raise HTTPException(status_code=404,detail="item not found")


            

@app.delete("/delete_book/{book_id}")
async def get_all_books(book_id:int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"removed":"successfully"}
    raise HTTPException(status_code=404,detail="item not found")


