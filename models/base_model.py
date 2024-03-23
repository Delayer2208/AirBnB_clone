"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
        """Represents the BaseModel of the AirBnB project."""

            def __init__(self, *args, **kwargs):
                        """Initialize a new BaseModel.

                                Args:
                                            *args (any): Unused.
                                                        **kwargs (dict): Key/value pairs of attributes.
                                                                """
                                                                        if kwargs:
                                                                                        for key, value in kwargs.items():
                                                                                                        if key == "created_at" or key == "updated_at":
                                                                                                                            value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                                                                                                                                            if key != "__class__":
                                                                                                                                                                setattr(self, key, value)
                                                                                                                                                                        else:
                                                                                                                                                                                    self.id = str(uuid4())
                                                                                                                                                                                                self.created_at = datetime.now()
                                                                                                                                                                                                            self.updated_at = datetime.now()
                                                                                                                                                                                                                        models.storage.new(self)

                                                                                                                                                                                                                            def save(self):
                                                                                                                                                                                                                                    """Update updated_at with the current datetime."""
                                                                                                                                                                                                                                            self.updated_at = datetime.now()
                                                                                                                                                                                                                                                    models.storage.save()

                                                                                                                                                                                                                                                        def to_dict(self):
                                                                                                                                                                                                                                                                """Return a dictionary representation of the BaseModel instance."""
                                                                                                                                                                                                                                                                        obj_dict = self.__dict__.copy()
                                                                                                                                                                                                                                                                                obj_dict["created_at"] = self.created_at.isoformat()
                                                                                                                                                                                                                                                                                        obj_dict["updated_at"] = self.updated_at.isoformat()
                                                                                                                                                                                                                                                                                                obj_dict["__class__"] = self.__class__.__name__
                                                                                                                                                                                                                                                                                                        return obj_dict

                                                                                                                                                                                                                                                                                                            def __str__(self):
                                                                                                                                                                                                                                                                                                                    """Return the string representation of the BaseModel instance."""
                                                                                                                                                                                                                                                                                                                            return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

                                                                                                                                                                                                                                                                                                                                @classmethod
                                                                                                                                                                                                                                                                                                                                    def from_dict(cls, obj_dict):
                                                                                                                                                                                                                                                                                                                                            """Create a new instance from a dictionary representation."""
                                                                                                                                                                                                                                                                                                                                                    obj_dict_copy = obj_dict.copy()
                                                                                                                                                                                                                                                                                                                                                            class_name = obj_dict_copy.pop("__class__", None)
                                                                                                                                                                                                                                                                                                                                                                    if class_name == cls.__name__:
                                                                                                                                                                                                                                                                                                                                                                                return cls(**obj_dict_copy)
                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                    raise ValueError("Invalid class name in dictionary representation")

