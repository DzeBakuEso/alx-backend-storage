#!/usr/bin/env python3
"""
Module: 101-students.py
ALX - 0x01-NoSQL
Returns all students sorted by average score in descending order.
"""

def top_students(mongo_collection):
    """
    Returns all students sorted by average score.
    
    Args:
        mongo_collection: pymongo collection object.

    Returns:
        List of students with an added field 'averageScore', sorted descending.
    """
    return list(mongo_collection.aggregate([
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": { "$avg": "$topics.score" }
            }
        },
        {
            "$sort": { "averageScore": -1 }
        }
    ]))
