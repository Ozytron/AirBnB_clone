#!/usr/bin/python3
"""City Model"""


from models.base_model import BaseModel


class City(BaseModel):
    """This is a class City that inherits from BaseModel
    Attributes:
        state_id (type: str): the id of the state where the city is.
        name (type: str): the name of the city.
    """
    state_id = ""
    name = ""