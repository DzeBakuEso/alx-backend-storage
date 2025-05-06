#!/usr/bin/env python3
"""
9-insert_school: Function that inserts a new document in a MongoDB collection
using keyword arguments (**kwargs).

This function inserts a new document into the collection with the attributes
passed in **kwargs, and returns the new document's _id.
"""

from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the given MongoDB collection with the provided
    keyword arguments.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: Keyword arguments representing the fields of the new document.
    
    Returns:
        str: The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
