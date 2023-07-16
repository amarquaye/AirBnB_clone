#!/usr/bin/python3
"""
This is the user creation class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """This defines attributes for user creation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
