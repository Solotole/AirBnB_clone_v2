#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

# from models.state import State
from os import getenv
# from models.base_model import BaseModel
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review
# from models.user import User
# from models.place import Place

engine_storage = getenv("HBNB_TYPE_STORAGE")
if engine_storage == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
elif engine_storage == "fs":
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
