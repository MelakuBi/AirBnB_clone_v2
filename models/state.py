#!/usr/bin/python3
"""This is the state class"""
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="delete", backref="state")
    else:
        @property
        def cities(self):
            my_list = []
            my_obj = models.storage.all(City)
            for key, value in my_obj.items():
                if value.state_id == self.id:
                    my_list.append(value)
            return my_list
