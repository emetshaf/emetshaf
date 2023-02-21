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


class BookFile(BaseModel, Base):
    __tablename__ = 'book_files'
    book_id = Column(String(60), ForeignKey('books.id'), nullable=False)
    language_id = Column(String(60), ForeignKey('languages.id'), nullable=False)
    cover = Column(String(500), nullable=False)
    file = Column(String(500), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(500), nullable=False)


class Book(BaseModel, Base):
    __tablename__ = 'books'
    name = Column(String(128), nullable=False)
    authors = relationship('Author', secondary="book_author",
                           viewonly=False)
    book_files = relationship('BookFile', backref='book', cascade='delete')
    reviews = relationship('Review', backref='book', cascade='delete')
