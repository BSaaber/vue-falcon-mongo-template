# Build and run
Put secrets to the settings file.
```
class MongoSettings:
    HOST = 'mongodb'
    PORT = 27017  # int(os.environ.get('MONGO_PORT'))
    USERNAME = 'admin'  # os.environ.get('MONGO_USERNAME')
    PASSWORD = 'admin'  # os.environ.get('MONGO_PASSWORD')
```
Build backend container.
```
cd backend
docker build -t back-only .
```
Create and start container for the first time.
```
docker run -p 3000:3000 --name back-only back-only
```
To start container for the next time:
```
docker start back-only
```
Backend will be available on your local machine on address ``localhost:3000``.

TODO - need database mocks. Now running backend only does not make sense because db.
# Development
``Httpie`` usage for api checking:
```
http --json GET http://localhost:3000/articles
```

[``Compass``](https://www.mongodb.com/try/download/compass) for db checking
# Troubleshooting
- *PyCharm does not resolve absolute imports.*

    File -> Settings -> Project -> Project Structure: mark ``backend`` directory as source root.
- *How to show errors?*

    Uncomment error handler in ``main.py``.