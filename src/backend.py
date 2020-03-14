import requests
from .DB import *
import os

def getrest(lat,lng,rad):
    try:
        res = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?key="+os.getenv('KEY')+"&location="+str(lat)+","+str(lng)+"&type=restaurant&radius="+str(rad))
    except:
        print("API Error")

    results = res.json()['results']

    for i in range(0,len(results)):

        restaurant = results[i]

        try:
            names = restaurant['name']
        except KeyError:
            names = "None"

        try:
            addresses = restaurant['vicinity']
        except KeyError:
            addresses = "None"

        try:
            priceRanges = restaurant['price_level']
        except KeyError:
            priceRanges = 0

        try:
            ratings = restaurant['rating']
        except KeyError:
            ratings = 0

        try:
            open = restaurant['opening_hours']
            isOpen = open['open_now']
        except KeyError:
            isOpen = False


        geo = restaurant['geometry']
        loc = geo['location']

        try:
            db_connect()
            Post(name = names, address = addresses, priceRange = priceRanges, rating = ratings, openNow = isOpen, location = loc).save()
        except:
            print("Database Error")
