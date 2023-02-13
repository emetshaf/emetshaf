import models
from models.base_model import Base, BaseModel
from models.audiobook import AudioBook
from models.author import Author
from models.book import Book
from models.language import Language
from models.narrator import Narrator
from models.review import Review
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


classes = {
    'AudioBook': AudioBook,
    'Author': Author,
    'Book': Book,
    'Language': Language,
    'Narrator': Narrator,
    'Review': Review,
    'User': User
    }


class Storage:
    __engine = None
    __session = None

    def __init__(self):
        EMETSHAF_MYSQL_USER = getenv('EMETSHAF_MYSQL_USER')
        EMETSHAF_MYSQL_PWD = getenv('EMETSHAF_MYSQL_PWD')
        EMETSHAF_MYSQL_HOST = getenv('EMETSHAF_MYSQL_HOST')
        EMETSHAF_MYSQL_DB = getenv('EMETSHAF_MYSQL_DB')
        EMETSHAF_ENV = getenv('EMETSHAF_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(EMETSHAF_MYSQL_USER, EMETSHAF_MYSQL_PWD, EMETSHAF_MYSQL_HOST, EMETSHAF_MYSQL_DB))

        if EMETSHAF_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dict[key] = obj
        return dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        self.__session.remove()

    def get(self, cls, id):
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def getAuth(self, username, password):

        all_cls = models.storage.all(User)
        for value in all_cls.values():
            if (value.username == username):
                if (value.password == password):
                    return True

        return None

    def count(self, cls=None):
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
