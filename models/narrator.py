from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Narrator(BaseModel, Base):
    __tablename__ = 'narrators'
    image = Column(String(500), nullable=True)
    first_name = Column(String(128), nullable=False)
    middle_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=False)
    audiobooks = relationship(
        'AudioBook', backref='narrator', cascade='delete')
