from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class BookBase(BaseModel):
    """
    Base schema for Book data

    Attributes:
        title: Book title (1-200 characters)
        author: Book author (1-100 characters)
        year: Publication year (optional, between 1000-2100)
    """

    title: str = Field(
        ..., min_length=1, max_length=200, description="Title of the book"
    )
    author: str = Field(
        ..., min_length=1, max_length=100, description="Author of the book"
    )
    year: Optional[int] = Field(None, ge=1000, le=2100, description="Publication year")


class BookCreate(BookBase):
    """Schema for creating a new book (POST requests)"""

    pass


class BookUpdate(BaseModel):
    """Schema for updating a book (PUT requests)"""

    title: Optional[str] = Field(None, min_length=1, max_length=200)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    year: Optional[int] = Field(None, ge=1000, le=2100)


class BookResponse(BookBase):
    """Schema for book responses (GET requests)"""

    id: int

    model_config = ConfigDict(from_attributes=True)
