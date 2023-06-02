# newuser - an app that responds to new user creation events on a stream

This is a super simple Python application that has no UI, just a single entry point that loops to read a Redis stream
and pull data from it, in this case user data, and I may add login data. It prints out the value it gets from the stream.

It could send an email or write data to a disk-based database, e.g., PostgreSQL or Snowflake.

The idea is to show how you can have a separate microservice handle "events" such as login or new user creation (or anything),
and process them asynchronously as well as separation of control. Redis streams make this super easy to do.

It's also a pattern for write-behind caching.

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
poetry run python app/new_user_service.py consumer
```

I may add some other options later, hence the command-line argument

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
Most of the code is in `app/new_user_service.py`
