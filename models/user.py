#!/usr/bin/python3
"""class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


class User(BaseModel, Base if (getenv("HBNB_TYPE_STORAGE")=="db") else object):
    """ USer class inherits from BaseModel"""
    __tablename__ = 'users'
    if HBNB_TYPE_STORAGE == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")        
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
