import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Text
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


class BookCategory(Base):
    __tablename__ = 'book_category'
    metadata = Base.metadata
    book_id = Column(String(60),
                     ForeignKey('books.id'),
                     nullable=False,
                     primary_key=True)
    category_id = Column(String(60),
                         ForeignKey('subcategories.id'),
                         nullable=False,
                         primary_key=True)


class Book(BaseModel, Base):
    __tablename__ = 'books'
    cover = Column(String(500), nullable=True)
    title = Column(String(128), nullable=False)
    language_id = Column(String(60), ForeignKey('languages.id'), nullable=True)
    authors = relationship('Author', secondary="book_author",
                           viewonly=False)
    categories = relationship('SubCategory', secondary="book_category",
                              viewonly=False)
    description = Column(Text, nullable=True)
    file = Column(String(500), nullable=True)
    reviews = relationship('Review', backref='book', cascade='delete')
    library = relationship('Library', backref="books", cascade='delete')
    favorites = relationship('Favorite', backref="books", cascade='delete')
    audiobooks = relationship('AudioBook', backref="books", cascade='delete')
