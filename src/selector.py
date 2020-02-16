import random
from .DB import *
import json

def randomizer():

    db_connect()

    list = dbget()

    x = random.randint(1,len(list))

    if(len(list)==0):
        return "List is empty, use filldb"
    else:
        return list[x]
