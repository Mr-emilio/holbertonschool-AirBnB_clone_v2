#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if HBNB_TYPE_STORAGE == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

    else:
        name = ""

    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances
        with state_id equals to the current State.id"""
        cities = []
        all_cities = models.storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                cities.append(city)
        return cities
