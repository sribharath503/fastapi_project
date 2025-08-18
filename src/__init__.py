from fastapi import FastAPI
from src.books.routes import book_router

Version="v1"
app=FastAPI(
    title="bookly",
    description="creating bookly app",
    version=Version
)

app.include_router(book_router,prefix="/api/{version}/books",tags=["books"])