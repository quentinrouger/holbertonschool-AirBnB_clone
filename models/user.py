#!/usr/bin/python3
"""
This module defines the class User.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class defines informations about User.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
