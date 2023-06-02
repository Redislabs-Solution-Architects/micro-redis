import os
import time

import requests

from utility import get_weather_endpoint
from utility import redis_conn


def get_weather(city):
    key = f"weather:{city}"

    start_time = time.time()

    # Try the cache first
    cache_entry = redis_conn.json().get(key)

    if cache_entry is not None:
        end_time = time.time()
        total_time = (end_time - start_time) * 1000
        print(f"Found in cache time: {total_time}")

        cache_entry["total_time"] = total_time
        cache_entry["from_cache"] = True
        return cache_entry
    else:
        api_key = os.getenv("WEATHER_API_KEY")

        if api_key is None:
            return {"Error": "No variable WEATHER_API_KEY defined"}

        url = get_weather_endpoint(city)
        try:
            response = requests.get(url)
            if response.status_code != 200:
                return response.json()

            weather_json = response.json()
            redis_conn.json().set(key, "$", weather_json)
            end_time = time.time()
            total_time = (end_time - start_time) * 1000
            print(f"Not found time: {total_time}")

            weather_json["total_time"] = total_time
            weather_json["from_cache"] = False
            return weather_json
        except Exception as ex:
            if len(ex.args) > 0:
                return {"Error": "Calling weather endpoint failed", "Message": ex.args[0]}
            else:
                return {"Error": "Calling weather endpoint failed", "Code": ex.code, "Message": ex.reason}
