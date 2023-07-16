#!/usr/bin/python3
"""
This defines city
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Defines city to look for"""
    state_id = ""
    name = ""
