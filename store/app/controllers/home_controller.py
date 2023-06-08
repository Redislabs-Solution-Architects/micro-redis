import os
import requests
from flask import render_template

from app.utility import redis_conn, session


def show_home(request):
    city = request.args.get("city", "Chicago")

    # Get the current weather for the city from our weather microservice
    # We'll use Redis as our "discovery service" to find other microservices
    weather_host = redis_conn.get("WEATHER_HOST")

    if weather_host is None:
        weather_host = os.getenv("WEATHER_HOST", "http://localhost:5000")

    url = f"{weather_host}/get_weather/{city}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather_json = response.json()
            temp = weather_json["main"]["temp"]
        else:
            temp = "Unknown"
    except requests.exceptions.ConnectionError:
        temp = "Unknown"

    user_name = ""
    email = session.get_session(request)

    if email:
        user = redis_conn.json().get(f"users:{email}")
        if user:
            user_name = f"{user['first_name']} {user['last_name']}"

    return render_template("index.html", name=user_name, city=city, temp=temp)
