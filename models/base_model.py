"""
BaseModel Class of Models Module
"""

from datetime import datetime
import json
import models
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from uuid import uuid4, UUID

"""
    Creates instance of Base if storage type is a database
    If not database storage, uses class Base
"""

Base = declarative_base()


class BaseModel:
    """
        attributes and functions for BaseModel class
    """

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
            instantiation of new BaseModel Class
        """
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()

    def __set_attributes(self, attr_dict):
        """
            private: converts attr_dict values to python class attributes
        """
        if 'id' not in attr_dict:
            attr_dict['id'] = str(uuid4())
        if 'created_at' not in attr_dict:
            attr_dict['created_at'] = datetime.utcnow()
        elif not isinstance(attr_dict['created_at'], datetime):
            attr_dict['created_at'] = datetime.strptime(
                attr_dict['created_at'], "%Y-%m-%d %H:%M:%S.%f"
            )
        if 'updated_at' not in attr_dict:
            attr_dict['updated_at'] = datetime.utcnow()
        elif not isinstance(attr_dict['updated_at'], datetime):
            attr_dict['updated_at'] = datetime.strptime(
                attr_dict['updated_at'], "%Y-%m-%d %H:%M:%S.%f"
            )
        for attr, val in attr_dict.items():
            setattr(self, attr, val)

    def __is_serializable(self, obj_v):
        """
            private: checks if object is serializable
        """
        try:
            obj_to_str = json.dumps(obj_v)
            return all(obj_to_str is not None,
                       isinstance(obj_to_str, str))
        except Exception:
            return False

    def bm_update(self, attr_dict=None):
        """
            updates the basemodel and sets the correct attributes
        """
        IGNORE = [
            'id', 'created_at', 'book_id',
            'author_id', 'language_id', 'category_id', 'updated_at'
        ]
        if attr_dict:
            updated_dict = {
                k: v for k, v in attr_dict.items() if k not in IGNORE
            }
            for key, value in updated_dict.items():
                setattr(self, key, value)
            self.save()

    def save(self):
        """
            updates attribute updated_at to current time
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_json(self):
        """
            returns json representation of self
        """
        obj_class = self.__class__.__name__
        bm_dict = {
            k: v if self.__is_serializable(v) else str(v)
            for k, v in self.__dict__.items()
        }
        if 'authors' in self.__dict__:
            bm_dict['authors'] = [a.to_json() for a in self.authors]
        if 'reviews' in self.__dict__:
            bm_dict['reviews'] = [r.to_json() for r in self.reviews]
        if 'audiobooks' in self.__dict__:
            bm_dict['audiobooks'] = [a.to_json() for a in self.audiobooks]
        if 'libraries' in self.__dict__:
            bm_dict['libraries'] = [lib.to_json() for lib in self.libraries]
        if 'favorites' in self.__dict__:
            bm_dict['favorites'] = [f.to_json() for f in self.favorites]
        bm_dict.pop('_sa_instance_state', None)
        bm_dict.update({
            '__class__': obj_class
        })
        if obj_class == 'User':
            bm_dict.pop('password', None)
        return (bm_dict)

    def __str__(self):
        """
            returns string type representation of object instance
        """
        class_name = type(self).__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)

    def delete(self):
        """
            deletes current instance from storage
        """
        models.storage.delete(self)
