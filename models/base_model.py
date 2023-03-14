#!/usr/bin/python3
"""The BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This is the base model that other classes will inherit"""
    def __init__(self, *args, **kwargs):
        """Initialization of the class
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """

        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, timeformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """This method updates the instance attribute 'updated_at'
        with the current datetime.
        -invoke save() function &
        - save to serialized file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """-This method returns a dictionary containing all
        keys/values of __dict__ of the instance.
        -A key __class__ is added to this dictionary with the
        class name of the object.
        -created_at and updated_at is converted to string object
        in ISO format using isoformat() of datetime object.
        """
        ret_dict = self.__dict__.copy()
        ret_dict["__class__"] = self.__class__.__name__
        ret_dict["created_at"] = self.created_at.isoformat()
        ret_dict["updated_at"] = self.updated_at.isoformat()

        return (ret_dict)

    def __str__(self):
        """return the Print/string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
