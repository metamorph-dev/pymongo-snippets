from pprint import pp

from bson import SON

from db_client import db

posts = db['posts']

result = posts.insert_many([
    {"x": 1, "tags": ["dog", "cat"]},
    {"x": 2, "tags": ["cat"]},
    {"x": 2, "tags": ["mouse", "cat", "dog"]},
    {"x": 3, "tags": []}
])

pipeline = [
    {"$unwind": "$tags"},
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}
]

pp(list(posts.aggregate(pipeline)))
