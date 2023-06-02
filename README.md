# Microservices with Python & Redis

This repo consists of 3 microservices written in Python that leverage Redis for caching, configuration, primary database,
and inter-service communication.

The goal is to simply demonstrate the following:

- API caching (see weather)
- session management (see store)
- configuration and user management (see store)
- inter-process communication using Redis streams (see store and newuser)

Each service has its own repo for installing and running.

Until I dockerize all this you'll want to run each service separately, on different ports.

- [Weather](/weather)
- [Store](/store)
- [Newuser](/newuser)
