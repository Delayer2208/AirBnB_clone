#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import Base


class CityModel(Base):
    """Represent a city.

    Attributes:
        state_id (str): The state id.
        city_name (str): The name of the city.
    """

    state_id = ""
    city_name = ""
