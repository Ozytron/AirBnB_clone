#!/usr/bin/python3
"""Place Model"""


from models.base_model import BaseModel


class Place(BaseModel):
    """This is a class Place that inherits from BaseModel
    Attributes:
        city_id (type: str): the id of the city (City.id).
        user_id (type: str): the id of the user (User.id).
        name (type:str): The name of the place.
        description (type:str): The description of the place.
        number_rooms (type:int): The number of rooms in the place.
        number_bathrooms (type:int): The number of bathrooms in the place.
        max_guest (type:int): The maximum number of guests in the place.
        price_by_night (type:int): The price by night of the place.
        latitude (type:float): The latitude of the place.
        longitude (type:float): The longitude of the place.
        amenity_ids (type:list): A list of Amenity ids.        """
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
    amenity_ids = []