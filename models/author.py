import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Author(BaseModel, Base):
    __tablename__ = 'authors'
    image = Column(String(500), nullable=True)
    first_name = Column(String(128), nullable=False)
    middle_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=False)
    book_authors = relationship('BookAuthor',
                                backref='authors',
                                cascade='delete')
