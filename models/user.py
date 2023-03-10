"""
User Class from Models Module
"""
from datetime import datetime, timedelta
from dotenv import load_dotenv
import hashlib
import jwt
import models
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from uuid import uuid4


load_dotenv()


class Library(Base):
    __tablename__ = 'libraries'
    metadata = Base.metadata
    user_id = Column(String(60), ForeignKey('users.id'),
                     nullable=False, primary_key=True)
    book_id = Column(String(60), ForeignKey('books.id'),
                     nullable=False, primary_key=True)


class Favorite(Base):
    __tablename__ = 'favorites'
    metadata = Base.metadata
    user_id = Column(String(60), ForeignKey('users.id'),
                     nullable=False, primary_key=True)
    book_id = Column(String(60), ForeignKey('books.id'),
                     nullable=False, primary_key=True)


class User(BaseModel, Base):
    """
        User class handles all application users
    """
    __tablename__ = 'users'
    username = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    libraries = relationship('Book', secondary="libraries", viewonly=False)
    favorites = relationship('Book', secondary="favorites", viewonly=False)
    reviews = relationship('Review', backref='user', cascade='delete')

    def __init__(self, *args, **kwargs):
        """
            instantiates user object
        """
        if kwargs:
            pwd = kwargs.pop('password', None)
            if pwd:
                User.__set_password(self, pwd)
                super().__init__(*args, **kwargs)

    def pass_encryption(pwd):
        """
        encrypts input to encypted string
        """
        secure = hashlib.md5()
        secure.update(pwd.encode("utf-8"))
        secure_password = secure.hexdigest()
        return secure_password

    def __set_password(self, pwd):
        """
            custom setter: encrypts password to MD5
        """
        secure_password = User.pass_encryption(pwd)
        setattr(self, "password", secure_password)

    def encode_auth_token(self, user_id):
        """
        Generates Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=0, seconds=60*60*24),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                os.environ.get(
                    'SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            print(e)
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, os.environ.get(
                'SECRET_KEY'), algorithms=["HS256"])
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError as e:
            print(e)
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError as e:
            print(e)
            return 'Invalid token. Please log in again.'


class BlacklistToken(BaseModel, Base):
    """
    Token Model for storing JWT tokens
    """
    if True:
        __tablename__ = 'blacklist_tokens'
        token = Column(String(500), unique=True, nullable=False)
        blacklisted_on = Column(
            DateTime, nullable=False, default=datetime.utcnow()
        )

        def __init__(self, token):
            """
            instantiates with BaseModel attributes
            """
            self.token = token
            self.blacklisted_on = datetime.utcnow()
            super().__init__()

        def __repr__(self):
            """_summary_
            """
            return '<id: token: {}'.format(self.token)

        @staticmethod
        def check_blacklist(auth_token):
            """
            check whether auth token has been blacklisted
            """
            all_tokens = models.storage.all('BlacklistToken').values()
            for token_obj in all_tokens:
                if token_obj.token == str(auth_token):
                    return True
            return False
