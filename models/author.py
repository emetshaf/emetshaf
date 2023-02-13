import models
from models.base_model import Base, BaseModel
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Author(BaseModel, Base):
    __tablename__ = 'authors'
    image = Column(String(500), nullable=True)
    pen_name = Column(String(128), nullable=True)
    first_name = Column(String(128), nullable=False)
    middle_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
