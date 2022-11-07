import datetime

from db_client import db


posts = db['posts']

post = {
    'author': 'Mike',
    'text': 'My first blog post!',
    'tags': ['mongodb', 'python', 'pymongo'],
    'date': datetime.datetime.utcnow(),
}

post_id = posts.insert_one(post).inserted_id
print(f'{post_id = }')
