# FastAPI and Docker

[![Continuous Integration and Delivery](https://github.com/marcusholmgren/fast-api-docker/actions/workflows/main.yml/badge.svg)](https://github.com/marcusholmgren/fast-api-docker/actions/workflows/main.yml)

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

Run the tests with coverage with [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/index.html).

```bash
docker-compose exec web python -m pytest --cov="."
```

Run formatting and linting with [ruff](https://astral.sh/ruff).
```bash
docker-compose exec web python -m ruff check
```


Stop the running containers with `docker-compose down` and then remove the stopped containers with `docker-compose rm`.

```bash
docker-compose down -v
```

### Docker Production

Build the production image

```bash
docker build -f project/Dockerfile.prod -t fastapi-docker ./project
```

#### Run the image locally

Run the production image locally with a sqlite in-memory database

```bash
docker run --name fastapi-docker -e PORT=8765 -e DATABASE_URL=sqlite:///:memory: -p 8002:8765 fastapi-docker:latest
```

Generate the required tables in the in-memory database. Connect to the running container and run the migrations from the `app/db.py` script.

```bash
docker exec -it fastapi-docker /bin/sh
source .venv/bin/activate
cd app/
python db.py
```

## Components

Tortoise-ORM migrations with [Aerich](https://tortoise.github.io/migration.html)