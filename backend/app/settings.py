import os


class MongoSettings:
    HOST = 'mongodb'
    PORT = int(os.environ.get('MONGO_PORT'))
    USERNAME = os.environ.get('MONGO_USERNAME')
    PASSWORD = os.environ.get('MONGO_PASSWORD')
