#!/usr/bin/python3
"""This is base_model"""
import uuid
from datetime import datetime
"""This is the Base module class in which other classes
inherits from
"""



class BaseModel:
<<<<<<< HEAD
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
=======
    def __init__(self, *args, **kwargs):
        """Initializes the class variables"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        if not kwargs:
            storage.new(self)

    def __str__(self):
        """returns objects in well printed string format"""
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Helper function to save the current state of data"""
>>>>>>> 610d9a638c584f389a709d8e05abc3a2f842f02a
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
<<<<<<< HEAD
        """returns dictionary format"""
=======
        """Converts the give data to dictionary"""
>>>>>>> 610d9a638c584f389a709d8e05abc3a2f842f02a
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
