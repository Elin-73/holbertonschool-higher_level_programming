#!/usr/bin/env python3
""" Code to insert the new school """
import pymongo


def insert_school(mongo_collection, **kwargs):
    new_school = mongo_collection.insert_one(kwargs)

    return (new_school.inserted_id)
