import models
from models.base_model import Base, BaseModel
import sqlalchemy
from sqlalchemy import Column, ForeignKey, String


class AudioBook(BaseModel, Base):
    __tablename__ = 'audiobooks'
    book_id = Column(String(128), ForeignKey('books.id'), nullable=False)
    narrator_id = Column(String(128), ForeignKey(
        'narrators.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
