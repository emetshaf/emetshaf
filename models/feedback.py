"""Catgory moddul
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Feedback(BaseModel, Base):
    __tablename__ = 'feedbacks'
    full_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    message = Column(String(128), nullable=False)
