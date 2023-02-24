import mongoengine as mongo

from app.settings import MongoSettings


class MongoClient:
    DB_NAME = 'base'

    def __init__(self):
        self.db = None

    def connect(self):
        self.db = mongo.connect(
            self.DB_NAME,
            host=MongoSettings.HOST,
            port=MongoSettings.PORT,
            username=MongoSettings.USERNAME,
            password=MongoSettings.PASSWORD
        )

    def disconnect(self):
        self.db.close()


db = MongoClient()
db.connect()
