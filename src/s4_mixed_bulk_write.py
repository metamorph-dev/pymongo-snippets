from pprint import pp

from pymongo import InsertOne
from pymongo import DeleteMany
from pymongo import ReplaceOne
from pymongo import UpdateOne

from db_client import db


posts = db['posts']

result = posts.bulk_write([
    DeleteMany({}),
    InsertOne({'_id': 1}),
    InsertOne({'_id': 2}),
    InsertOne({'_id': 3}),
    UpdateOne({'_id': 1}, {'$set': {'foo': 'bar'}}),
    UpdateOne({'_id': 4}, {'$inc': {'j': 1}}, upsert=True),
    ReplaceOne({'j': 1}, {'j': 2}),
])

pp(result.bulk_api_result)
