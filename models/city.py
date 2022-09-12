#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


class City(BaseModel, Base if (getenv("HBNB_TYPE_STORAGE")=="db") else object):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if HBNB_TYPE_STORAGE == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        name = ""
        state_id = ""

    if HBNB_TYPE_STORAGE == "db":
        def __init__(self, *args, **kwargs):
            """initializes city"""
            super().__init__(*args, **kwargs)
