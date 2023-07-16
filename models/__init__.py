#!/usr/bin/python3
""" We import all modules and packages """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
