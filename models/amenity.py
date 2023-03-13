#!/usr/bin/python3
"""Amenity Model"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """This is a class Amenity that inherits from BaseModel
    Attributes:
        name (type: str): the name of the Amenity.
    """
    name = ""