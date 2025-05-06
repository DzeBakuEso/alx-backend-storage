#!/usr/bin/env python3
"""
11-schools_by_topic: Function to find all schools with a specific topic.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have a specific topic.

    Args:
        mongo_collection: A pymongo collection object.
        topic (str): The topic to search for.
    
    Returns:
        list: Documents where 'topics' field contains the given topic.
    """
    return list(mongo_collection.find({"topics": topic}))
