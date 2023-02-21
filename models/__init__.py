import os
from models.base_model import BaseModel
from models.user import User
from models.user import BlacklistToken

"""CNC - dictionary = { Class Name (string) : Class Type }"""

from models.engine import storage
CNC = storage.Storage.CNC
storage = storage.Storage()

storage.reload()
