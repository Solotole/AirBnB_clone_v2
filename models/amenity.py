#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """ Amenity class model """
    __tablename__ = "amenities"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("PlaceAmenity", backref=place_amenity)
    else:
        name = ""
        def __init__(self, *args, **kwargs):
            """initializes Amenity"""
            super().__init__(*args, **kwargs)
