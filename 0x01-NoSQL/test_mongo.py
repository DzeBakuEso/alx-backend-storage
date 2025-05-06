# test_mongo.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.test_database
print("Collections:", db.list_collection_names())
