# models/engine/file_storage.py

import json


class FileStorage:
        """Serializes instances to JSON file and deserializes JSON file to instances"""

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
                                                                                            serialized = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
                                                                                                    with open(FileStorage.__file_path, 'w') as file:
                                                                                                                    json.dump(serialized, file)

                                                                                                                        def reload(self):
                                                                                                                                    """Deserializes the JSON file to __objects"""
                                                                                                                                            try:
                                                                                                                                                            with open(FileStorage.__file_path, 'r') as file:
                                                                                                                                                                                data = json.load(file)
                                                                                                                                                                                                for key, value in data.items():
                                                                                                                                                                                                                        class_name, obj_id = key.split('.')
                                                                                                                                                                                                                                            obj_dict = value
                                                                                                                                                                                                                                                                module = __import__('models.' + class_name, fromlist=[class_name])
                                                                                                                                                                                                                                                                                    cls = getattr(module, class_name)
                                                                                                                                                                                                                                                                                                        instance = cls(**obj_dict)
                                                                                                                                                                                                                                                                                                                            FileStorage.__objects[key] = instance
                                                                                                                                                                                                                                                                                                                                    except FileNotFoundError:
                                                                                                                                                                                                                                                                                                                                                    pass

