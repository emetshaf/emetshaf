import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Language(BaseModel, Base):
    __tablename__ = 'languages'
    code = Column(String(128), nullable=False)
    country = Column(String(1024), nullable=False)
    books = relationship("Book",
                         backref="language",
                         cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
