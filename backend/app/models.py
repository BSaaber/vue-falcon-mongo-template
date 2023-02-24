from mongoengine import Document, StringField


class Article(Document):
    title = StringField(max_length=100, reqired=True)
    text = StringField(required=True)
