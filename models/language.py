import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Language(BaseModel, Base):
    __tablename__ = 'languages'
    name = Column(String(128), nullable=False)
    book_authors = relationship('BookFile',
                                backref='languages',
                                cascade='delete')
