# fast-api-docker

This is my implementation of the project in the  [testdriven.io](https://testdriven.io/) course 
[Test-Driven Development with FastAPI and Docker](https://testdriven.io/courses/tdd-fastapi/)


## Docker Compose

Start
```
docker-compose up -d --build 
```

Stop containers and volumes
```
docker-compose down -v
```


Generate database schema
```
docker-compose exec web python app/db.py
```

## Tests

```
docker-compose exec web python -m pytest
```

### Code Coverage

Console output
```
docker-compose exec web python -m pytest --cov="."
```

HTML report
```
docker-compose exec web python -m pytest --cov="." --cov-report html
```

Checking formatting and structure of code.

Linting with flake8

```
docker-compose exec web flake8 ./app
```


Format with black

```
docker-compose exec web black ./app --check
```

Check python imports

```
docker-compose exec web /bin/sh -c "isort ./app/**/*.py --check-only"
```


Built on top of:
* [FastAPI](https://fastapi.tiangolo.com) framework, high performance, easy to learn, fast to code, ready for production
* [Tortoise ORM](https://tortoise-orm.readthedocs.io/en/latest/index.html#) is an easy-to-use `asyncio` ORM (_Object Relational Mapper_) inspired by Django.
* [PostgreSQL](https://www.postgresql.org): The World's Most Advanced Open Source Relational Database
* [Heroku](https://www.heroku.com) Cloud Application Platform


