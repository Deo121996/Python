import pymongo
from pymongo import MongoClient



def get_database_list():
    client = MongoClient("localhost",27017)
    list_db= client.list_database_names()
    if "aa" in list_db:
        return True
    return False
