#!/usr/bin/env python3
""" Is there any way to read this? """

def list_all(mongo_collection):
    documents: list = []

    for document in mongo_collection.find():
        documents.append(document)

    return documents
