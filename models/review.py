#!/usr/bin/python3
"""
This module defines the class Review.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class defines informations about reviews.
    """
    place_id = ""
    user_id = ""
    text = ""
