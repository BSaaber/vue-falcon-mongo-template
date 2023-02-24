import falcon
import json

from app.mongo import db
from app.models import Article


class Handler:
    ROUTE = '/handler'

    async def on_get(self, req, resp):
        """Handle GET request"""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = 'hello world from backend simple get handler'


class ArticleHandler:
    ROUTE = '/articles'

    async def on_get(self, req, resp):
        articles = []
        for article in Article.objects:
            articles.append(article.title + ': ' + article.text)

        resp.status = falcon.HTTP_200
        resp.media = {
            'stat': 200,
            'articles': articles,
        }

    async def on_post(self, req, resp):
        new_article = Article(
            title='Big Title',
            text='Article text. Some words. Some more words.',
        )
        new_article.save()

        resp.status = falcon.HTTP_201
