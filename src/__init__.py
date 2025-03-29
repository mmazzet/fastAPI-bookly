from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"server is starting...")
    yield
    print(f"server has been stopped")

version = "v1"

# The info below will appear on the Swagger documentation
app = FastAPI(
    title="Bookly",
    decription="A RestAPI for a book review web service",
    version = version,
    lifespan=life_span
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])