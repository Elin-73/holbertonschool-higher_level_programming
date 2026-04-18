#!/usr/bin/env python3
""" WE IMPORT PYMONGO """
import pymongo


def schools_by_topic(mongo_collection, topic: str):
    """ HERE DICT LIST, FOR EACH SCHOOL WE ADD WE APPEND IT TO A LIST """
    query: dict = { "topics" : topic }
    schools: list = []

    for school in mongo_collection.find(query):
        schools.append(school)

    return schools
