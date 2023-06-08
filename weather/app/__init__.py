import json

from flask import Flask
from flask import render_template
from flask import request

from app import weather

app = Flask(__name__)


def to_pretty_json(value):
    return json.dumps(value, sort_keys=True,
                      indent=4, separators=(',', ': '))


app.jinja_env.filters['tojson_pretty'] = to_pretty_json


@app.route("/")
def index():
    return "Index"


@app.route("/hello")
def hello_world():
    return "Hello friend."


@app.route("/weather")
def render_weather():
    city = request.args.get("city", "Oakland")
    the_weather = get_weather(city)
    return render_template("weather.html", city=city, weather=the_weather)


@app.route("/get_weather/<city>")
def get_weather(city):
    return weather.get_weather(city)
