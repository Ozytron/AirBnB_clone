#!/usr/bin/python3
"""User Model"""


from models.base_model import BaseModel


class User(BaseModel):
    """This is a class User that inherits from BaseModel
    Attributes:
        email (type:str): the email of the user
        password (type:str): the password of the user
        first_name (type:str): the first name of the user
        last_name (type:str): the last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
