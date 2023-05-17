import os

import redis

redis_conn = redis.StrictRedis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=os.getenv("REDIS_PORT", 6379),
    password=os.getenv("REDIS_PASS", ""),
    encoding="utf-8", decode_responses=True)
