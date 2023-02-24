import falcon.asgi
# import traceback

from app.handlers.handler import Handler, ArticleHandler

app = falcon.asgi.App(
    middleware=[
        falcon.CORSMiddleware(allow_origins=['http://localhost'], allow_credentials='*'),
    ])

app.add_route(Handler.ROUTE, Handler())
app.add_route(ArticleHandler.ROUTE, ArticleHandler())


# async def handle_all_exceptions(req, resp, exc, params):
#     print(exc)
#     print(traceback.format_exc())
#
#
# app.add_error_handler(Exception, handle_all_exceptions)
