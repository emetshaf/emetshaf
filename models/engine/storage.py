"""
Database engine
"""
from dotenv import load_dotenv
from os import environ
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models import audiobook, author, base_model, book, category, feedback, language, narrator, review, user

load_dotenv()

EMETSHAF_MYSQL_USER = environ.get('EMETSHAF_MYSQL_USER')
EMETSHAF_MYSQL_PWD = environ.get('EMETSHAF_MYSQL_PWD')
EMETSHAF_MYSQL_HOST = environ.get('EMETSHAF_MYSQL_HOST')
EMETSHAF_MYSQL_DB = environ.get('EMETSHAF_MYSQL_DB')
EMETSHAF_ENV = environ.get("EMETSHAF_ENV")


class Storage:
    """
        handles long term storage of all class instances
    """
    CNC = {
        'AudioBook': audiobook.AudioBook,
        'Author': author.Author,
        'Book': book.Book,
        'Category': category.Category,
        'Feedback': feedback.Feedback,
        'Language': language.Language,
        'Narrator': narrator.Narrator,
        'Review': review.Review,
        'SubCategory': category.SubCategory,
        'User': user.User,
        'BlacklistToken': user.BlacklistToken
    }

    """
        handles storage for database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
            creates the engine self.__engine
        """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}?charset=utf8mb4'.format(
                EMETSHAF_MYSQL_USER, EMETSHAF_MYSQL_PWD,
                EMETSHAF_MYSQL_HOST, EMETSHAF_MYSQL_DB)
        )
        if EMETSHAF_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
           returns a dictionary of all objects
        """
        obj_dict = {}
        if cls is not None:
            a_query = self.__session.query(Storage.CNC[cls])
            for obj in a_query:
                obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                if (cls == 'Book') and obj.authors and obj.reviews:
                    pass
                if (cls == 'User') and obj.libraries and obj.favorites:
                    pass
                obj_dict[obj_ref] = obj
            return obj_dict

        for c in Storage.CNC.values():
            a_query = self.__session.query(c)
            for obj in a_query:
                obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[obj_ref] = obj
        return obj_dict

    def new(self, obj):
        """
            adds objects to current database session
        """
        self.__session.add(obj)

    def save(self):
        """
            commits all changes of current database session
        """
        self.__session.commit()

    def rollback_session(self):
        """
            rollsback a session in the event of an exception
        """
        self.__session.rollback()

    def delete(self, obj=None):
        """
            deletes obj from current database session if not None
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def delete_all(self):
        """
           deletes all stored objects, for testing purposes
        """
        for c in Storage.CNC.values():
            a_query = self.__session.query(c)
            all_objs = [obj for obj in a_query]
            for obj in range(len(all_objs)):
                to_delete = all_objs.pop(0)
                to_delete.delete()
        self.save()

    def reload(self):
        """
           creates all tables in database & session from engine
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))

    def close(self):
        """
            calls remove() on private session attribute (self.session)
        """
        self.__session.remove()

    def get(self, cls, id):
        """
            retrieves one object based on class name and id
        """
        if cls and id:
            fetch = "{}.{}".format(cls, id)
            all_obj = self.all(cls)
            return all_obj.get(fetch)
        return None

    def count(self, cls=None):
        """
            returns the count of all objects in storage
        """
        return (len(self.all(cls)))
