from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.reviews.routes import review_router
from contextlib import asynccontextmanager
from src.db.main import init_db
from .errors import register_all_errors

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"server is starting...")
    await init_db()
    yield
    print(f"server has been stopped")

version = "v1"

# The info below will appear on the Swagger documentation
app = FastAPI(
    title="Bookly",
    decription="A RestAPI for a book review web service",
    version = version,
)

register_all_errors(app)


app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=['auth'])
app.include_router(review_router, prefix=f"/api/{version}/reviews", tags=['reviews'])