"""This module provides translation capabilities for multiple languages
    using google API.
"""
import json
import pymongo
from pymongo import  InsertOne

# db = client.mydata
client = pymongo.MongoClient("mongodb://localhost:27017/")
# Create a new database
db = client["mydatabase1"]
collection = db.listingAndReviews
requesting = []

with open("listingsAndReviews.json", encoding='utf-8') as f:
    for jsonObj in f:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))
        print("inserted")

result = collection.bulk_write(requesting)
client.close()
