import models
from models.base_model import Base, BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

book_author = Table('book_author', Base.metadata,
                    Column('book_id', String(60),
                           ForeignKey('books.id', onupdate='CASCADE',
                                      ondelete='CASCADE'),
                           primary_key=True),
                    Column('author_id', String(60),
                           ForeignKey('authors.id', onupdate='CASCADE',
                                      ondelete='CASCADE'),
                           primary_key=True))


class Book(BaseModel, Base):
    __tablename__ = 'books'
    cover = Column(String(500), nullable=True)
    title = Column(String(128), nullable=False)
    authors = relationship("Author",
                           secondary=book_author,
                           viewonly=False)
    language_id = Column(String(60), ForeignKey('languages.id'), nullable=False)
    audiobook = relationship("AudioBook", uselist=False, backref="book", cascade="all, delete, delete-orphan")
    reviews = relationship("Review", backref="book",
                           cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
