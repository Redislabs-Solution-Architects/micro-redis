# Weather - a weather microservice using Redis for API caching

## Prerequisites

- Python 3.11 or greater
- Poetry (because I like Poetry)
- Redis
- [Open Weather Map API Key ](https://openweathermap.org/api)

## Installing

```bash
poetry install
```

## Running
```bash
poetry shell
poetry run flask run
```

## Docker
You may run all three service plus the Redis database from docker. We've provided docker-compose files for each service,
as well as for Redis. You must build each service image, then run docker-compose to bring them up.

By default, weather is listening on port 5050, store on 5051, Redis on 6379

```bash
docker-compose -f weather/docker-compose.yml build
docker-compose -f store/docker-compose.yml build
docker-compose -f newuser/docker-compose.yml build
docker-compose -f docker-compose.yml -f weather/docker-compose.yml -f store/docker-compose.yml -f newuser/docker-compose.yml up -d
docker logs new-user-app
```


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
Most of the code is in `app/weather.py`

There are utility functions in `utility/__init__.py`

## Endpoints
By default, flask runs on port 5000. There are many ways to change that, including the `-p <port>` option to `flask run`

So the default URL is `http://localhost:5000`. Note that flask sometimes doesn't allow access to `localhost` by default. 
I never use localhost because there are so many problems with that

There are three endpoints:
- `/` is just the home page
- `/weather?city=<city>` is the JSON dump of the weather data in a web page
- `/get_weather/<city>` is the RESTful API to get just the JSON weather data

The JSON returned has two additional fields added:
- `from_cache` true or false
- `total_time` in milliseconds