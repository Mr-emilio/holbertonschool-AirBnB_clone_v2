#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship



class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances
        with state_id equals to the current State.id"""
        from models import storage
        from models.city import City
        cities = []
        for key, value in storage.all(City).items():
            if value.state_id == self.id:
                cities.append(value)
        return cities
