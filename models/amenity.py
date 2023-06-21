#!/usr/bin/python3
"""This is the amenity class"""
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), primary_key=True, nullable=True)
        place_amenities = relationship("Place", secondary="place_amenity")
    else:
        name = ""
