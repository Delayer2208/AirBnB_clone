#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
        """Serializes instances to a JSON file and deserializes JSON file to instances"""

            __file_path = "file.json"
                __objects = {}

                    def all(self):
                                """Returns the dictionary __objects"""
                                        return FileStorage.__objects

                                        def new(self, obj):
                                                    """Sets in __objects the obj with key <obj class name>.id"""
                                                            key = "{}.{}".format(obj.__class__.__name__, obj.id)
                                                                    FileStorage.__objects[key] = obj

                                                                        def save(self):
                                                                                    """Serializes __objects to the JSON file (path: __file_path)"""
                                                                                            serialized = {}
                                                                                                    for key, obj in FileStorage.__objects.items():
                                                                                                                    serialized[key] = obj.to_dict()
                                                                                                                            with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
                                                                                                                                            json.dump(serialized, f)

                                                                                                                                                def reload(self):
                                                                                                                                                            """Deserializes the JSON file to __objects"""
                                                                                                                                                                    try:
                                                                                                                                                                                    with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                                                                                                                                                                                                        data = json.load(f)
                                                                                                                                                                                                                        for key, value in data.items():
                                                                                                                                                                                                                                                class_name, obj_id = key.split('.')
                                                                                                                                                                                                                                                                    class_lookup = {"BaseModel": BaseModel, "User": User, "State": State,
                                                                                                                                                                                                                                                                                                                "City": City, "Place": Place, "Amenity": Amenity, "Review": Review}
                                                                                                                                                                                                                                                                                        obj = class_lookup[class_name](**value)
                                                                                                                                                                                                                                                                                                            FileStorage.__objects[key] = obj
                                                                                                                                                                                                                                                                                                                    except FileNotFoundError:
                                                                                                                                                                                                                                                                                                                                    pass

