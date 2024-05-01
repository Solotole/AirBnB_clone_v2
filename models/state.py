#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import String, Column, orm


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = orm.relationship("City", backref="state",
                                cascade="all, delete-orphan")

    @property
    def cities:
        """ function that returns the list of City instances
            with state_id equals to the current State.id
        """
        from models import storage
        important_list = []
        single_cities = storage.all(City).keys()
        for single_city in single_cities.values():
            if self.id == single_city.state_id:
                important_list.append(single_city)
        return important_list
