from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class AudioBook(BaseModel, Base):
    __tablename__ = 'audiobooks'
    file = Column(String(500), nullable=False)
    book_id = Column(String(60), ForeignKey('books.id'), nullable=True)
    narrator_id = Column(String(60), ForeignKey('narrators.id'), nullable=True)
