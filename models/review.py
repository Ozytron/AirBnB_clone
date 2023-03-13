#!/usr/bin/python3
"""Review Model"""


from models.base_model import BaseModel


class Review(BaseModel):
    """This is a class Review that inherits from BaseModel
    Attributes:
        place_id (type: str): the id of the city (Place.id).
        user_id (type: str): the id of the user (User.id).
        text (type:str): user's review of the place.
    """
    place_id = ""
    user_id = ""
    text = ""