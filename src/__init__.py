from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"

# The info below will appear on the Swagger documentation
app = FastAPI(
    title="Bookly",
    decription="A RestAPI for a book review web service",
    version = version
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])