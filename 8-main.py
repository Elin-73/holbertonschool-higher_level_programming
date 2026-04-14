#!/usr/bin/env python3
""" main for 8 """
from pymongo import MongoClient
list_all = __import__("8-all").list_all

if __name__ == "__main__":
    client = MongoClient("mongodb")
