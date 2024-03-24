#!/usr/bin/python3
"""File Storage implementation."""

import json
from my_models.base_model import MyCustomBase
from my_models.user import CustomUserModel
from my_models.state import CustomStateModel
from my_models.city import CustomCityModel
from my_models.place import CustomPlaceModel
from my_models.amenity import CustomAmenityModel
from my_models.review import CustomReviewModel


class MyCustomFileStorage:
        """Implementation of a storage engine using JSON files."""

            FILE_PATH = "custom_file.json"
                OBJECTS = {}

                    def get_all(self):
                                """Return all stored objects."""
                                        return self.OBJECTS

                                        def add_new(self, obj):
                                                    """Add a new object to the storage."""
                                                            key = f"{obj.__class__.__name__}.{obj.id}"
                                                                    self.OBJECTS[key] = obj

                                                                        def save_data(self):
                                                                                    """Serialize objects to JSON file."""
                                                                                            serialized = {}
                                                                                                    for key, value in self.OBJECTS.items():
                                                                                                                    serialized[key] = value.to_dict()
                                                                                                                            with open(self.FILE_PATH, "w") as file:
                                                                                                                                            json.dump(serialized, file)

                                                                                                                                                def load_data(self):
                                                                                                                                                            """Deserialize JSON file to objects."""
                                                                                                                                                                    try:
                                                                                                                                                                                    with open(self.FILE_PATH, "r") as file:
                                                                                                                                                                                                        deserialized = json.load(file)
                                                                                                                                                                                                                        for key, value in deserialized.items():
                                                                                                                                                                                                                                                class_name = value['__class__']
                                                                                                                                                                                                                                                                    del value['__class__']
                                                                                                                                                                                                                                                                                        obj = eval(class_name)(**value)
                                                                                                                                                                                                                                                                                                            self.OBJECTS[key] = obj
                                                                                                                                                                                                                                                                                                                    except FileNotFoundError:
                                                                                                                                                                                                                                                                                                                                    pass


