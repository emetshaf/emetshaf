from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey


class AudioBook(BaseModel, Base):
    __tablename__ = 'audiobooks'
    file = Column(String(500), nullable=False)
