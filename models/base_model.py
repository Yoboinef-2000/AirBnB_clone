#!/usr/bin/python3

"""Import the uuid, datetime modules."""
import uuid
import datetime
import models

"""The base model class."""

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    """The base model class."""

    def __init__(self, *args, **kwargs):
        """Initialize instances."""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue

                if key in ['created_at', 'updated_at']:
                    theformat = "%Y-%m-%dT%H:%M:%S.%f"
                    value = datetime.datetime.strptime(value, theformat)
                setattr(self, key, value)
        # if kwargs:
        #    for key, value in kwargs.items():
        #        if key != "__class__":
        #            setattr(self, key, value)
        # if hasattr(self, "created_at") and type(self.created_at) is str:
        #   self.created_at = datetime.strptime(kwargs["created_at"], time)
        # if hasattr(self, "updated_at") and type(self.updated_at) is str:
        #   self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Return custom string representation."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the public instance atrribute updated_at with
        the current datetime.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of
        the instance with additional information for serialization.
        """
        allDict = self.__dict__.copy()
        allDict['__class__'] = self.__class__.__name__
        allDict['created_at'] = self.created_at.isoformat()
        allDict['updated_at'] = self.updated_at.isoformat()
        return (allDict)
