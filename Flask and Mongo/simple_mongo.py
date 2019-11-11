import pymongo

def get_connection():
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017', socketTimeoutMS=12000)
    return client

#insert data

def insert_data(database,collection, data):
    """
    funcion to insert data
    :param data:
    :return success:
    """
    client = get_connection()
    success = client[database][collection].insert_one(data)
    return success

def fetch_data(database, collection, filter={}, projection={'_id':0}):
    """
    funcion to get data
    :param database:
    :param collection:
    :param filter:
    :return records:
    """
    client = get_connection()
    records = client[database][collection].find(filter,projection)
    return list(records)

resp = fetch_data('tea','cups')
print("\n\n")
print(resp)
