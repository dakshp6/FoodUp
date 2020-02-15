import random
from .DB import *


def randomizer():

    x = random.randint(1,21)

    db_connect()

    list = dbget()

    return list[x]
