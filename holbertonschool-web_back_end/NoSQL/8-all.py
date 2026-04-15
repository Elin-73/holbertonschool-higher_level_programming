#!/usr/bin/env python3
""" 8-all code """

def list_all(mongo_collection):
    return list(mongo_collection.find())
