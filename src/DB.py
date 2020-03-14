from mongoengine import *
import json
import os

def db_connect():
    connect('FoodUp',username = os.getenv('DB_USER'),password = os.getenv('DB_PASS'),host = os.getenv('DBHOST'))


def dbget():


    res = Post.objects
    ls = []
    for x in res:
        sol = x.to_json()
        ls.append(json.loads(sol))

    return ls


def dbdel():

    for posts in Post.objects:
        posts.delete()


class Post(Document):

    name = StringField(required=True)
    address = StringField(required=True)
    priceRange = IntField(required=True)
    rating = DecimalField(required=True)
    openNow = BooleanField(required=True)
    location = DictField(required=True)
    meta = {'collection': os.getenv('COLLECTION_NAME')}
