from .models import books_model
from sqlalchemy.orm import session
from .schemas import BookModel,UpdateBookModel
from sqlalchemy import delete




def create(db:session,create_book_model:BookModel):
    db_book=books_model(**create_book_model.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def all_books(db:session):
    db_get_books=db.query(books_model).all()
    return db_get_books

def book(db:session,Book_id:int):
    db_get_book=db.query(books_model).filter(books_model.id ==Book_id ).first()
    return db_get_book

def update(db:session,Book_id:int,update_book:UpdateBookModel):
    db_update_book=db.query(books_model).filter(books_model.id == Book_id).first()
    if db_update_book:
        for key,value in update_book.model_dump(exclude_unset=True).items():
            setattr(db_update_book,key,value)
    db.commit()
    db.refresh(db_update_book)
    return db_update_book

def delete(db:session,Book_id:int):
    db_delete_book=db.query(books_model).filter(books_model.id == Book_id).first()
    if db_delete_book:
        db.delete(db_delete_book)
        db.commit()
        db.refresh(db_delete_book)
    return db_delete_book

    