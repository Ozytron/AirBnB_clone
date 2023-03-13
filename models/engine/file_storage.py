#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode="w", encoding="utf-8") as write_file:
            storage_dict = {}
            for key, value in self.__objects.items():
                storage_dict[key] = value.to_dict()
            json.dump(storage_dict, write_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doest
        exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as j_data:
                for obj in json.load(j_data).values():
                    Cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(Cls_name)(**obj))
        except FileNotFoundError:
            return
