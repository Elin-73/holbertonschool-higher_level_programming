#!/usr/bin/env python3
""" 8-all code """

def list_all(mongo_collection):
    """ Return a list of what is found in mongo collection"""
    return list(mongo_collection.find())
