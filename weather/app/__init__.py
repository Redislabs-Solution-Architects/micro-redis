import json
import os
import time
import urllib.request

from flask import Flask
from flask import render_template
from flask import request

from utility import redis_conn
from utility import get_weather_endpoint

app = Flask(__name__)


@app.route("/")
def index():
    return "Index"


@app.route("/hello")
def hello_world():
    return "Hello friend."


@app.route("/weather")
def render_weather():
    city = request.args.get("city", "Oakland")
    weather = get_weather(city)
    return render_template("weather.html", city=city, weather=weather)


@app.route("/get_weather/<city>")
def get_weather(city):
    start_time = time.time()

    key = f"weather:${city}"
    # Try the cache first
    cache_entry = redis_conn.json().get(key)

    if cache_entry is not None:
        end_time = time.time()
        print(f"From cache time: {(end_time - start_time) * 1000}")
        return cache_entry
    else:
        api_key = os.getenv("WEATHER_API_KEY")

        if api_key is None:
            return {"Error": "No variable WEATHER_API_KEY defined"}

        url = get_weather_endpoint(city)
        try:
            response = urllib.request.urlopen(url)
            data = response.read()
            weather_json = json.loads(data)
            end_time = time.time()
            print(f"Cache miss time: {(end_time - start_time) * 1000}")
            redis_conn.json().set(key, "$", weather_json)
            return weather_json
        except Exception as ex:
            if len(ex.args) > 0:
                return {"Error": "Calling weather endpoint failed", "Message": ex.args[0]}
            else:
                return {"Error": "Calling weather endpoint failed", "Code": ex.code, "Message": ex.reason}
