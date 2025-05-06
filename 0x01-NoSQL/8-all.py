#!/usr/bin/env python3
"""
8-all: Function that lists all documents in a MongoDB collection.

This function connects to the MongoDB collection passed as the parameter and 
returns a list of all documents present in the collection.
"""

from pymongo import MongoClient

def list_all(mongo_collection):
    """
    Lists all documents in the given MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.
    
    Returns:
        list: A list of all documents in the collection, or an empty list 
              if the collection is empty.
    """
    return list(mongo_collection.find())
