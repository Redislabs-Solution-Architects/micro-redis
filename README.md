# Microservices with Python & Redis

This repo consists of 3 microservices written in Python that leverage Redis for caching, configuration, primary database,
and inter-service communication.

The goal is to simply demonstrate the following:

- API caching (see weather)
- session management (see store)
- configuration and user management (see store)
- inter-process communication using Redis streams (see store and newuser)

Each service has its own repo for installing and running.

- [Weather](/weather)
- [Store](/store)
- [Newuser](/newuser)

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

