from hashlib import md5
import models
from models.base_model import Base, BaseModel
import sqlalchemy
from sqlalchemy import Column, String


class User(BaseModel, Base):
    __tablename__ = 'user'
    username = Column(String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        if name == 'password':
            value = md5(value.encode()).hexdigest()
        return super().__setattr__(name, value)
