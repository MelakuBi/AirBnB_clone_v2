#!/usr/bin/python3
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ Class """
    __engine = None
    __session = None

    def __init__(self):
        """ Public instance method """
        my_user = getenv("HBNB_MYSQL_USER")
        my_pwd = getenv("HBNB_MYSQL_PWD")
        my_host = getenv("HBNB_MYSQL_HOST")
        my_db = getenv("HBNB_MYSQL_DB")
        my_env = getenv("HBNB_ENV")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(my_user, my_pwd, my_host,
                                              my_db), pool_pre_ping=True)
        if "test" == my_env:
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Public instance method """
        my_list = []
        my_dict = {}
        if cls is None:
            my_list = [User, State, City, Place, Review]
            for i in my_list:
                qry = self.__session.query(i)
                for i in qry:
                    item = "{}.{}".format(type(i).__name__, i.id)
                    my_dict[item] = i
        else:
            if type(cls) is str:
                cls = eval(cls)
            qry = self.__session.query(cls)
            for i in qry:
                item = "{}.{}".format(type(i).__name__, i.id)
                my_dict[item] = i
        return (my_dict)

    def new(self, obj):
        """ Public instance method """
        self.__session.add(obj)

    def save(self):
        """ Public instance method """
        self.__session.commit()

    def delete(self, obj=None):
        """ Public instance method """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """ Public instance method """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()

    def close(self):
        """ Public instance method """
        self.__session.close()
