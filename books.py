from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List


app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django by example",
        "author": "Antonio Mele",
        "publisher": "Pakt",
        "published_date": "2022-01-19",
        "page_count": 1203,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The web socket handbook",
        "author": "Alex Diaconu",
        "publisher": "Wang",
        "published_date": "2022-01-18",
        "page_count": 1209,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Pinocchio",
        "author": "Collodi",
        "publisher": "Rizzoli",
        "published_date": "2022-01-18",
        "page_count": 1234,
        "language": "Italian",
    },
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


@app.get("/books/{book_id}")
async def get_book(book_id: int) -> dict:
    pass


@app.get("/books/{book_id}")  # DELETE
async def delete_book(book_id: int) -> dict:
    pass
