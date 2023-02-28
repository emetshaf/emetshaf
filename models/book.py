import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class BookAuthor(Base):
    __tablename__ = 'book_author'
    metadata = Base.metadata
    book_id = Column(String(60),
                     ForeignKey('books.id'),
                     nullable=False,
                     primary_key=True)
    author_id = Column(String(60),
                       ForeignKey('authors.id'),
                       nullable=False,
                       primary_key=True)


class Book(BaseModel, Base):
    __tablename__ = 'books'
    cover = Column(String(500), nullable=True)
    title = Column(String(128), nullable=False)
    language_id = Column(String(60), ForeignKey('languages.id'), nullable=True)
    authors = relationship('Author', secondary="book_author",
                           viewonly=False)
    description = Column(String(500), nullable=True)
    file = Column(String(500), nullable=True)
    reviews = relationship('Review', backref='book', cascade='delete')
    library = relationship('Library', backref="books", cascade='delete')
    favorites = relationship('Favorite', backref="books", cascade='delete')
