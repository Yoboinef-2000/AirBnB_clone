#!/usr/bin/python3

"""Import BaseModel."""
from models.base_model import BaseModel

"""Class User."""


class User(BaseModel):
    """Class User."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initilaize instances."""
        super().__init__(*args, **kwargs)
