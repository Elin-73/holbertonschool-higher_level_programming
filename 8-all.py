#!/usr/bin/env python3
""" Is there any way to read this? """
import pymongo

def list_all(mongo_collection) -> list:
    documents: list = []

    for document in mongo_collection.find():
        documents.append(document)

    return documents
