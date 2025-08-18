from fastapi import APIRouter,HTTPException
from .book_datas import books
from .schemas import BookModel,UpdateBookModel




book_router=APIRouter()



@book_router.get("/get_all_books")
async def get_all_books():
    return books

@book_router.get("/get_book/{book_id}")
async def get_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="book not found")

@book_router.post("/create_book")
async def create_book(book_data:BookModel):
    new_book=book_data.model_dump()
    books.append(new_book)
    return new_book


@book_router.patch("/update_book/{book_id}")
async def update_book(book_id:int,update_book_data:UpdateBookModel):
    for book in books:
        if book["id"] == book_id:
            book["title"]=update_book_data.title
            book["author"]=update_book_data.author
            book["year"]=update_book_data.year
            book["genre"]=update_book_data.genre

            return book
    
    raise HTTPException(status_code=404,detail="item not found")


            

@book_router.delete("/delete_book/{book_id}")
async def get_all_books(book_id:int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"removed":"successfully"}
    raise HTTPException(status_code=404,detail="item not found")
