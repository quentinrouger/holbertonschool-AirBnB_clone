#!/usr/bin/python3
"""
This module defines the class FileStorage.
"""


from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json
import os


class FileStorage:
    """
    Write a class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return the dictionary __object
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        add a new object to __object
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Method that serializes __objects to the JSON file."""
        object = {}
        for key, value in FileStorage.__objects.items():
            object[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(object, file)

    def reload(self):
        """
        Deserialize the JSON file to '__objects' if the file exists.
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                object = json.load(file)
                for key, value in object.items():
                    FileStorage.__objects[key] =\
                        eval(value['__class__'])(**value)
        except Exception:
            return
