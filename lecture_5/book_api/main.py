from typing import List, Optional

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy import or_
from sqlalchemy.orm import Session

from . import models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/books/", response_model=schemas.BookResponse)
def create_book(
    book: schemas.BookCreate, db: Session = Depends(get_db)
) -> schemas.BookResponse:
    """
    Create a new book in the collection.

    Args:
        book (schemas.BookCreate): The book data to create
        db (Session): Database session dependency

    Returns:
        schemas.BookResponse: The created book with its ID

    Raises:
        HTTPException: If there's a database error (500 status code)
    """
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=List[schemas.BookResponse])
def read_books(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
) -> List[schemas.BookResponse]:
    """
    Get all books with pagination support.

    Args:
        skip (int): Number of records to skip (for pagination)
        limit (int): Maximum number of records to return (1-100)
        db (Session): Database session dependency

    Returns:
        List[schemas.BookResponse]: List of books in the collection
    """
    return db.query(models.Book).offset(skip).limit(limit).all()


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    """
    Delete a book by its ID.

    Args:
        book_id (int): The ID of the book to delete
        db (Session): Database session dependency

    Returns:
        dict: Confirmation message

    Raises:
        HTTPException: If the book with given ID is not found (404)
    """
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}


@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(
    book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)
) -> schemas.BookResponse:
    """
    Update book details by ID.

    Args:
        book_id (int): The ID of the book to update
        book_update (schemas.BookUpdate): New book data
        db (Session): Database session dependency

    Returns:
        schemas.BookResponse: The updated book

    Raises:
        HTTPException: If the book with given ID is not found (404)
    """
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Get only fields that were actually sent
    update_data = book_update.model_dump(exclude_unset=True)

    # Loop through ONLY the sent fields
    for key, value in update_data.items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book


@app.get("/books/search/", response_model=List[schemas.BookResponse])
def search_books(
    title: Optional[str] = Query(None),
    author: Optional[str] = Query(None),
    year: Optional[int] = Query(None),
    db: Session = Depends(get_db),
) -> List[schemas.BookResponse]:
    """
    Search books by title, author, or year.

    Args:
        title (Optional[str]): Search by title (partial match, case-insensitive)
        author (Optional[str]): Search by author (partial match, case-insensitive)
        year (Optional[int]): Search by exact publication year
        db (Session): Database session dependency

    Returns:
        List[schemas.BookResponse]: List of books matching the search criteria
    """
    query = db.query(models.Book)
    conditions = []

    if title:
        conditions.append(models.Book.title.ilike(f"%{title}%"))
    if author:
        conditions.append(models.Book.author.ilike(f"%{author}%"))
    if year:
        conditions.append(models.Book.year == year)

    if conditions:
        query = query.filter(or_(*conditions))

    return query.all()
