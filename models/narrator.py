import models
from models.base_model import Base, BaseModel
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Narrator(BaseModel, Base):
    __tablename__ = 'narrators'
    first_name = Column(String(128), nullable=False)
    middle_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    audiobooks = relationship("AudioBook", backref="narrator",
                              cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
