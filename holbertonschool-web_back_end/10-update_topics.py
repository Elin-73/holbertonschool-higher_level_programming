#!/usr/bin/env python3
""" Update School """
import pymongo
from typing import List


def update_topics(mongo_collection, name, topics):
    query: dict = { "name" : name }
    mongo_collection.update_many( query, { "$set" : { "topics" : topics }})
