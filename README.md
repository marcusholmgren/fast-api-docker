# FastAPI and Docker
Test-Driven Development with FastAPI and Docker


## Docker Compose

Build the images and start the containers with `docker-compose up`.

```bash
docker-compose up -d --build
```

Run the migrations with `docker-compose exec web aerich upgrade`.

```bash
docker-compose exec web aerich upgrade
```

Run the tests with `docker-compose exec web pytest`.

```bash
docker-compose exec web python -m pytest
```

Stop the running containers with `docker-compose down` and then remove the stopped containers with `docker-compose rm`.

```bash
docker-compose down -v
```

## Components

Tortoise-ORM migrations with [Aerich](https://tortoise.github.io/migration.html)