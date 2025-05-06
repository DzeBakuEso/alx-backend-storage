#!/usr/bin/env python3
"""
10-update_topics: Function that updates the topics of a school document
based on the school's name.
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of a school document where the 'name' matches.

    Args:
        mongo_collection: A pymongo collection object.
        name (str): The name of the school to update.
        topics list of str): The list of topics to set for the school.
    
    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
