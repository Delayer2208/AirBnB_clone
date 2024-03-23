# models/base_model.py

import uuid
from datetime import datetime
from models import storage


class BaseModel:
        """BaseModel class that defines attributes id, created_at, updated_at, and methods"""

            def __init__(self, *args, **kwargs):
                        """Constructor for BaseModel class"""
                                if not kwargs:
                                                self.id = str(uuid.uuid4())
                                                            self.created_at = datetime.now()
                                                                        self.updated_at = datetime.now()
                                                                                    storage.new(self)
                                                                                            else:
                                                                                                            for key, value in kwargs.items():
                                                                                                                                if key != "__class__":
                                                                                                                                                        if key in ["created_at", "updated_at"]:
                                                                                                                                                                                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                                                                                                                                                                                                        setattr(self, key, value)

                                                                                                                                                                                                            def save(self):
                                                                                                                                                                                                                        """Update the updated_at attribute with the current datetime and save the changes"""
                                                                                                                                                                                                                                self.updated_at = datetime.now()
                                                                                                                                                                                                                                        storage.save()

                                                                                                                                                                                                                                            def to_dict(self):
                                                                                                                                                                                                                                                        """Return a dictionary representation of the BaseModel instance"""
                                                                                                                                                                                                                                                                my_dict = self.__dict__.copy()
                                                                                                                                                                                                                                                                        my_dict.update({
                                                                                                                                                                                                                                                                                        "__class__": self.__class__.__name__,
                                                                                                                                                                                                                                                                                                    "updated_at": self.updated_at.isoformat(),
                                                                                                                                                                                                                                                                                                                "created_at": self.created_at.isoformat()
                                                                                                                                                                                                                                                                                                                        })
                                                                                                                                                                                                                                                                                return my_dict

