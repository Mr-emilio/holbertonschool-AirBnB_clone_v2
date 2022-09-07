#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy import create_engine
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User


class DBStorage:
    '''Class db storage'''
    alvclasses = {"State": State, "City": City}
    __engine = None
    __session = None

    def __init__(self):
        '''Constructor'''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''Returns a dictionary of models currently in storage'''
        new_dict = {}
        if cls is None:
            for key, value in self.alvclasses.items():
                for obj in self.__session.query(value).all():
                    new_dict[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for obj in self.__session.query(cls).all():
                new_dict[obj.__class__.__name__ + '.' + obj.id] = obj
        return new_dict

    def new(self, obj):
        '''Adds new object to storage dictionary'''
        self.__session.add(obj)

    def save(self):
        '''Saves storage dictionary to file'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete obj from __objects if it’s inside'''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''Loads storage dictionary from file'''
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine, expire_on_commit=False)()