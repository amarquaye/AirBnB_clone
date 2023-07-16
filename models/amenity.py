#!/usr/bin/python3
"""
This defines amenities
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines the amenities that user can choose from to offer at its place"""
    name = ""
