from fastapi import FastAPI
from src.books.routes import book_router
from .db import engine,Base

Version="v2"
app=FastAPI(
    title="bookly",
    description="creating bookly app",
    version=Version
)

Base.metadata.create_all(bind=engine)

app.include_router(book_router,prefix="/api/{version}/books",tags=["books"])