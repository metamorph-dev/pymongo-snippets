import datetime
from pprint import pp

from db_client import db


posts = db['posts']

new_posts = [
    {
        'author': 'Mike',
        'text': 'Another posts!',
        'tags': ['bulk', 'insert'],
        'date': datetime.datetime(2009, 11, 12, 11, 14),
    },
    {
        'author': 'Eliot',
        'title': 'MongoDB if fun',
        'text': 'and pretty easy too!',
        'date': datetime.datetime(2009, 11, 10, 10, 45),
    }
]

result = posts.insert_many(new_posts).inserted_ids
pp(result, indent=2)
