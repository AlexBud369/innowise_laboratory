from sqlalchemy import Column, Integer, String

from .database import Base


class Book(Base):
    """
    Book model representing a book in the collection.

    Attributes:
        id: Primary key, unique identifier
        title: Book title (required, max 200 chars)
        author: Book author (required, max 100 chars)
        year: Publication year (optional)
    """

    __tablename__ = "books"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String(200), nullable=False)
    author: str = Column(String(100), nullable=False)
    year: int | None = Column(Integer, nullable=True)
