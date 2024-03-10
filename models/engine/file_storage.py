#!/usr/bin/python3

"""Import modules and classes."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


here = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
"""Class File Storage."""


class FileStorage():
    """Class FileStorage."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return (self.__objects)

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        if obj:
            self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        json_ob = {}
        for key in self.__objects:
            json_ob[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_ob, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                json_data = json.load(file)
            # for key in json_data:
            #     className = json_data
            #     self.__objects[key] = BaseModel(**json_data[key])
            for key in json_data:
                class_name = json_data[key].get("__class__", "")
                if class_name in self.here:
                    class_instance = globals()[class_name](**json_data[key])
                    self.__objects[key] = class_instance
        except Exception:
            pass
