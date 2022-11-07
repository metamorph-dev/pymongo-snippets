from environs import Env


env = Env()
env.read_env()

MONGO_URL = env('MONGO_URL')
DB_NAME = env('DB_NAME')
