#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import Base


class FileStorage:
        """Represents a simplified storage engine using JSON files.

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
                                                                                    if obj:
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
                                                                                                                                                                                                                                                                                            class_name = value.get('__class__')
                                                                                                                                                                                                                                                                                                                if class_name and 'id' in value:
                                                                                                                                                                                                                                                                                                                                            del value['__class__']
                                                                                                                                                                                                                                                                                                                                                                    obj = eval(class_name)(**value)
                                                                                                                                                                                                                                                                                                                                                                                            self.__objects[key] = obj
                                                                                                                                                                                                                                                                                                                                                                                                    except FileNotFoundError:
                                                                                                                                                                                                                                                                                                                                                                                                                    pass
                                                                                                                                                                                                                                                                                                                                                                                                                        except Exception as e:
                                                                                                                                                                                                                                                                                                                                                                                                                                        print(f"Error loading from file: {e}")


