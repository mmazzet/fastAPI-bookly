from contextlib import asynccontextmanager

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from src.auth.routes import auth_router
from src.books.routes import book_router
from src.db.main import init_db
from src.reviews.routes import review_router

from .errors import register_all_errors
from .middleware import register_middleware


@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"server is starting...")
    await init_db()
    yield
    print(f"server has been stopped")


version = "v1"

# The info below will appear on the Swagger documentation
app = FastAPI(
    lifespan=life_span,
    title="Bookly",
    description="A RestAPI for a book review web service",
    version=version,
    license_info = {
        "name":"MIT",
        "url":"https://opensource.org/licenses/mit"
    },
    docs_url=f"/api/{version}/docs",
    redoc_url=f"/api/{version}/redoc",
    openapi_url=f"/api/{version}/openapi.json",
    contact={
        "name":"The company",
        "email": "company@mymail.com",
        "url": "https://thegoodcompany.io"
    },
)



register_all_errors(app)

register_middleware(app)


app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=["auth"])
app.include_router(review_router, prefix=f"/api/{version}/reviews", tags=["reviews"])


@app.get("/", include_in_schema=False)
def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Welcome to the Bookly API. Visit /api/v1/docs for API docs."}
    )
