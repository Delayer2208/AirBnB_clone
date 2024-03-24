#!/usr/bin/python3
"""Defines the Base class for all models."""
import models
from uuid import uuid4
from datetime import datetime


class Base:
        """Base class for all models."""

            def __init__(self, *args, **kwargs):
                        """Initialize a new Base instance.

                                Args:
                                                *args (any): Unused.
                                                            **kwargs (dict): Key/value pairs of attributes.
                                                                    """
                                                                            time_format = "%Y-%m-%dT%H:%M:%S.%f"
                                                                                    self.id = str(uuid4())
                                                                                            self.created_at = datetime.today()
                                                                                                    self.updated_at = datetime.today()
                                                                                                            if len(kwargs) != 0:
                                                                                                                            for k, v in kwargs.items():
                                                                                                                                                if k == "created_at" or k == "updated_at":
                                                                                                                                                                        self.__dict__[k] = datetime.strptime(v, time_format)
                                                                                                                                                                                        else:
                                                                                                                                                                                                                self.__dict__[k] = v
                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                        models.storage_engine.new(self)

                                                                                                                                                                                                                                            def save(self):
                                                                                                                                                                                                                                                        """Update updated_at with the current datetime."""
                                                                                                                                                                                                                                                                self.updated_at = datetime.today()
                                                                                                                                                                                                                                                                        models.storage_engine.save()

                                                                                                                                                                                                                                                                            def to_dict(self):
                                                                                                                                                                                                                                                                                        """Return the dictionary representation of the Base instance."""
                                                                                                                                                                                                                                                                                                rdict = self.__dict__.copy()
                                                                                                                                                                                                                                                                                                        rdict["created_at"] = self.created_at.isoformat()
                                                                                                                                                                                                                                                                                                                rdict["updated_at"] = self.updated_at.isoformat()
                                                                                                                                                                                                                                                                                                                        rdict["__class__"] = self.__class__.__name__
                                                                                                                                                                                                                                                                                                                                return rdict

                                                                                                                                                                                                                                                                                                                                def __str__(self):
                                                                                                                                                                                                                                                                                                                                            """Return the string representation of the Base instance."""
                                                                                                                                                                                                                                                                                                                                                    clname = self.__class__.__name__
                                                                                                                                                                                                                                                                                                                                                            return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

