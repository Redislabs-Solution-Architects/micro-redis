import os
import urllib

import redis

redis_conn = redis.StrictRedis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=os.getenv("REDIS_PORT", 6379),
    password=os.getenv("REDIS_PASS", ""),
    encoding="utf-8", decode_responses=True)


def get_weather_endpoint(city):
    api_key = os.getenv("WEATHER_API_KEY")
    # Be sure to use the https protocol since we're passing the API key
    encoded_city = urllib.parse.quote_plus(city)
    return f"https://api.openweathermap.org/data/2.5/weather?q={encoded_city}&units=imperial&appid={api_key}"
