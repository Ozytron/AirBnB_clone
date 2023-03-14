#!/usr/bin/python3
"""FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """The storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(name, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, mode="w") as write_file:
            storage_dict = {}
            for key, value in FileStorage.__objects.items():
                storage_dict[key] = value.to_dict()
            json.dump(storage_dict, write_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doest
        exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, mode="r") as j_data:
                for obj in json.load(j_data).values():
                    Cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(Cls_name)(**obj))
        except FileNotFoundError:
            return
