#!/usr/bin/python3
"""class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """ USer class inherits from BaseModel"""
    __tablename__ = 'users'
    if HBNB_TYPE_STORAGE == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", cascade="all,delete",
                backref=backref("user", cascade="all,delete"),
                passive_deletes=True,
                single_parent=True)
        reviews = relationship("Review", cascade="all,delete",
                backref=backref("user", cascade="all,delete"),
                passive_deletes=True,
                single_parent=True)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
