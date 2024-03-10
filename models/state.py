#!/usr/bin/python3

"""Import BaseModel."""
from models.base_model import BaseModel

"""Class State."""


class State(BaseModel):
    """Class State."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initilaize instances."""
        super().__init__(*args, **kwargs)
