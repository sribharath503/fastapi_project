from fastapi import APIRouter,HTTPException,Depends
from .models import books_model
from .schemas import BookModel,UpdateBookModel,book_out
from .crud import *
from src.db import get_db



book_router=APIRouter()



@book_router.get("/get_all_books",response_model=list[book_out])
async def get_all_books(db:session=Depends(get_db)):
    return  all_books(db)

@book_router.get("/get_book/{Book_id}",response_model=book_out)
async def get_book(Book_id:int,db:session=Depends(get_db)):
   new_book= book(db,Book_id)
   if not new_book:
       raise HTTPException(status_code=404,detail="book not found")
   return new_book

@book_router.post("/create_book",response_model=book_out)
async def create_book(create_book_model:BookModel,db:session=Depends(get_db)):
    new_book= create(db,create_book_model)
    return new_book


@book_router.patch("/update_book/{Book_id}",response_model=book_out)
async def update_book(Book_id:int,update_book:UpdateBookModel,db:session=Depends(get_db)):
    new_book= update(db,Book_id,update_book)
    if not new_book:
        raise HTTPException(status_code=404,detail="book not found")
    return new_book
            

@book_router.delete("/delete_book/{Book_id}",response_model=book_out,status_code=200)
async def delete_books(Book_id:int,db:session=Depends(get_db)):
    new_book= delete(db,Book_id)
    return new_book
