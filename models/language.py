import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Language(BaseModel, Base):
    __tablename__ = 'languages'
    name = Column(String(128), nullable=False)
    books = relationship('Book',
                         backref='languages',
                         cascade='delete')
