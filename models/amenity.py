#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

class Amenity(BaseModel, Base):
    """class amenity"""
    __tablename__ = 'amenities'
    if HBNB_TYPE_STORAGE == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place",
                          secondary="place_amenity",
                          viewonly=False,
                          back_populates="amenities")
    else:
        name = ""
