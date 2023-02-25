"""Catgory moddul
"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    __tablename__ = 'categories'
    name = Column(String(128), nullable=False)
    subcategories = relationship('SubCategory',
                                 backref='categories',
                                 cascade='delete')


class SubCategory(BaseModel, Base):
    __tablename__ = 'subcategories'
    name = Column(String(128), nullable=False)
    category_id = Column(String(60), ForeignKey(
        'categories.id'), nullable=True)
