import random
from .DB import *
import json

def randomizer():

    x = random.randint(1,21)

    db_connect()

    list = json.dumps(dbget())

    return list
