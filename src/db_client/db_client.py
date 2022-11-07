from pymongo import MongoClient

from . import config


client = MongoClient(config.MONGO_URL)
db = client[config.DB_NAME]
