#!/usr/bin/python3
"""
This module defines the class BaseModel.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base class for other classes, providing common attributes and methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel object.

        Args:
            id (str): The unique identifier for the object.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime
                                (value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
         Return a string representation of the BaseModel object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the public instance attribute 'updated_at' with the current
        datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys and values of the instance's
        __dict__.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
