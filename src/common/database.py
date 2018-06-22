import pymongo
import os


class Database(object):
    URI = os.environ.get('MONGODB_URI')
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client.get_default_database()

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query_id, data):
        return Database.DATABASE[collection].update_one(query_id, data, upsert=False)

    @staticmethod
    def sort(collection, sort_query, num):
        return Database.DATABASE[collection].find().sort(sort_query, num)