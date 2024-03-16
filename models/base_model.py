#!/usr/bin/python3
"""This is base_model"""
import uuid
from datetime import datetime



class BaseModel:
    """This is Base model class"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Converts an object to String readable format"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """makes saves and updates time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns dictionary format"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
