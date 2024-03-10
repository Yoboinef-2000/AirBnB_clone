#!/usr/bin/python3

"""Import BaseModel."""
from models.base_model import BaseModel

"""Class Amenity."""


class Amenity(BaseModel):
    """Class Amenity."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initilaize instances."""
        super().__init__(*args, **kwargs)
