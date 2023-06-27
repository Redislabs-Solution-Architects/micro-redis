# Store - a storefront ecommerce app

This is a really bare bones "e-commerce" app that supports user signup, login, and shopping cart management, all using
Redis as the database. It uses Flask as the web server since it's so easy to get up and running.

It also works with a couple of microservices to demonstrate how one might connect microservices using Redis.

## Prerequisites

- Python 3.11 or greater
- Poetry (because I like Poetry)
- Redis

## Installing

```bash
poetry install
```

## Running
```bash
poetry shell
poetry run python flask run
```

## Docker
To run with Docker see the parent folder README

## Testing
```bash
poetry run pytest
```

Note the tests rely on a running Redis. I'll update this someday to use https://testcontainers-python.readthedocs.io/en/latest/README.html.

For now, it's easiest to just run the docker redis-stack image, e.g.,
```bash
docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
```

## Code
The main "router" for the various endpoints is found in `app/__init.py__`. From there you should be able to trace the
rest of the code.

Controllers are in `app/controllers`
Utility functions are in `app/utility`
