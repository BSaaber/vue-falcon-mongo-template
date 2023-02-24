# Deployment
Todo
# Development
Todo
# Build and run
- Install and run [docker desktop](https://www.docker.com/products/docker-desktop/) or install docker [by cli](https://docs.docker.com/engine/install/ubuntu/)

- Clone git repository.
```
git clone git@github.com:BSaaber/vue-falcon-mongo-template.git
```
- Enter project directory.
```
cd vue_falcon_mongo_template
```
- Create ``.env`` file.
```
printf 'MONGO_ROOT_USERNAME=<username>\nMONGO_ROOT_PASSWORD=<password>\nMONGO_PORT=<port>' > .env
```
For example:
```
printf 'MONGO_ROOT_USERNAME=admin\nMONGO_ROOT_PASSWORD=admin\nMONGO_PORT=27017' > .env
```
- Build.
```
docker-compose build
```
- Run.
```
docker-compose up
```