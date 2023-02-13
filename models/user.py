from hashlib import md5
import models
from models.base_model import Base, BaseModel
import sqlalchemy
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import relationship


library = Table('library', Base.metadata,
                    Column('book_id', String(60),
                           ForeignKey('books.id', onupdate='CASCADE',
                                      ondelete='CASCADE'),
                           primary_key=True),
                    Column('user_id', String(60),
                           ForeignKey('users.id', onupdate='CASCADE',
                                      ondelete='CASCADE'),
                           primary_key=True))

favourite = Table('favourite', Base.metadata,
                    Column('book_id', String(60),
                           ForeignKey('books.id', onupdate='CASCADE',
                                      ondelete='CASCADE'),
                           primary_key=True),
                    Column('user_id', String(60),
                           ForeignKey('users.id', onupdate='CASCADE',
                                      ondelete='CASCADE'),
                           primary_key=True))

class User(BaseModel, Base):
    __tablename__ = 'users'
    username = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    reviews = relationship("Review", backref="user", cascade="all, delete, delete-orphan")
    library = relationship("User",
                           secondary=library,
                           viewonly=False)
    favourite = relationship("User",
                           secondary=favourite,
                           viewonly=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        if name == 'password':
            value = md5(value.encode()).hexdigest()
        return super().__setattr__(name, value)
