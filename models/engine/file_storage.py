#!/usr/bin/python3
"""Defines a storage engine using JSON files."""

import json
from models.base_model import BaseModel
from models.user import UserModel
from models.state import StateModel
from models.city import CityModel
from models.place import PlaceModel
from models.amenity import AmenityModel
from models.review import ReviewModel


class FileStorage:
        """Represents a storage engine using JSON files.

            Attributes:
                    __file_path (str): The path to the JSON file.
                            __objects (dict): A dictionary to store all objects by their IDs.
                                """
                                    __file_path = "file.json"
                                        __objects = {}

                                            def all(self):
                                                        """Returns the dictionary __objects."""
                                                                return self.__objects

                                                                def new(self, obj):
                                                                        """Adds a new object to the storage dictionary."""
                                                                                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                                                                                        self.__objects[key] = obj

                                                                                            def save(self):
                                                                                                    """Serializes __objects to the JSON file."""
                                                                                                            serialized = {}
                                                                                                                    for key, value in self.__objects.items():
                                                                                                                                serialized[key] = value.to_dict()
                                                                                                                                        with open(self.__file_path, "w") as file:
                                                                                                                                                    json.dump(serialized, file)

                                                                                                                                                        def reload(self):
                                                                                                                                                                """Deserializes the JSON file to __objects."""
                                                                                                                                                                        try:
                                                                                                                                                                                    with open(self.__file_path, "r") as file:
                                                                                                                                                                                                    deserialized = json.load(file)
                                                                                                                                                                                                                    for key, value in deserialized.items():
                                                                                                                                                                                                                                        class_name = value['__class__']
                                                                                                                                                                                                                                                            del value['__class__']
                                                                                                                                                                                                                                                                                obj = eval(class_name)(**value)
                                                                                                                                                                                                                                                                                                    self.__objects[key] = obj
                                                                                                                                                                                                                                                                                                            except FileNotFoundError:
                                                                                                                                                                                                                                                                                                                        pass

