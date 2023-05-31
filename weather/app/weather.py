import os

import requests

from utility import get_weather_endpoint
from utility import redis_conn


def get_weather(city):
    key = f"weather:${city}"

    # Try the cache first
    cache_entry = redis_conn.json().get(key)

    if cache_entry is not None:
        return cache_entry
    else:
        api_key = os.getenv("WEATHER_API_KEY")

        if api_key is None:
            return {"Error": "No variable WEATHER_API_KEY defined"}

        url = get_weather_endpoint(city)
        try:
            response = requests.get(url)
            weather_json = response.json()
            redis_conn.json().set(key, "$", weather_json)
            return weather_json
        except Exception as ex:
            if len(ex.args) > 0:
                return {"Error": "Calling weather endpoint failed", "Message": ex.args[0]}
            else:
                return {"Error": "Calling weather endpoint failed", "Code": ex.code, "Message": ex.reason}
