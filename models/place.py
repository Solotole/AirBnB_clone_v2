#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Integer, Float, Table
from os import getenv
from sqlalchemy.orm import relationship
import models


place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id', String(60), ForeignKey('places.id'),
            nullable=False, primary_key=True),
        Column(
            'amenity_id', String(60), ForeignKey('amenities.id'),
            nullable=False, primary_key=True)
        )


class Place(BaseModel, Base):
    """class Place
    Attributes:
        city_id (str): City ID.
        user_id (str): User ID.
        name (str): Place name.
        description (str): Place description.
        number_rooms (int): Number of rooms.
        number_bathrooms (int): Number of bathrooms.
        max_guest (int): Maximum number of guests.
        price_by_night (int): Price per night.
        latitude (float): Latitude.
        longitude (float): Longitude.
        amenity_ids (list of str): List of amenities.
    """
    __tablename__ = "places"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60, collation='latin1_swedish_ci'), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        amenities = relationship(
                            "Amenity", secondary=place_amenity,
                            back_populates="place_amenities",
                            viewonly=False)
        reviews = relationship("Review", passive_deletes=True, backref="place")
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        reviews = []
        amenity_ids = []

        @property
        def reviews(self):
            """
            get reviews
            """
            reviews_dict = models.storage.all(models.Review)
            reviews_list = []
            for review in reviews_dict.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review

        @property
        def amenities(self):
            """
            Gets the list of Amenity objects
            """
            obj_list = []
            objs = models.storage.all('Amenity')
            for amenity in objs.values():
                if amenity.id in self.amenity_ids:
                    obj_list.append(amenity)
            return obj_list

        @amenities.setter
        def amenities(self, obj):
            """
            Sets an amenity to Place
            """
            if isinstance(obj, Amenity):
                if self.id == obj.place_id:
                    self.amenity_ids.append(obj.id)

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
