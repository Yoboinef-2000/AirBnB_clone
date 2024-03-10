#!/usr/bin/python3

"""Import BaseModel."""
from models.base_model import BaseModel

"""Class Review."""


class Review(BaseModel):
    """Class Review."""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initilaize instances."""
        super().__init__(*args, **kwargs)
