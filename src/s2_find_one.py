from pprint import pp

from db_client import db


posts = db['posts']

post = posts.find_one({'author': 'Mike'})
pp(post, indent=2)
