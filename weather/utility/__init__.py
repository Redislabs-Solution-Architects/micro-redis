import os
import urllib

import redis

from dotenv import load_dotenv

load_dotenv()

redis_conn = redis.StrictRedis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=os.getenv("REDIS_PORT", 6379),
    password=os.getenv("REDIS_PASS", ""),
    encoding="utf-8",
    decode_responses=True)


weather_ttl = redis_conn.get("weather_ttl")
if weather_ttl is None:
    weather_ttl = 60


def get_weather_endpoint(city):
    api_key = os.getenv("WEATHER_API_KEY")
    endpoint = os.getenv("WEATHER_ENDPOINT")

    # Be sure to use the https protocol since we're passing the API key
    encoded_city = urllib.parse.quote_plus(city)
    return f"{endpoint}?q={encoded_city}&units=imperial&appid={api_key}"
