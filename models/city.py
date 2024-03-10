#!/usr/bin/python3

"""Import BaseModel."""
from models.base_model import BaseModel

"""Class City."""


class City(BaseModel):
    """Class City."""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initilaize instances."""
        super().__init__(*args, **kwargs)
