import hashlib
import json
import urllib

from flask import render_template, make_response, redirect

from app.utility import redis_conn, session


def show_home(request):
    city = request.args.get("city", "Chicago")

    # Get the current weather for the city from our weather microservice
    encoded_city = urllib.parse.quote_plus(city)
    url = f"http://epreston.io:5050//get_weather/{encoded_city}"
    response = urllib.request.urlopen(url)
    data = response.read()
    weather_json = json.loads(data)
    temp = weather_json["main"]["temp"]

    user_name = "Nobody"
    email = session.get_session(request)

    if email:
        user = redis_conn.json().get(f"users:{email}")
        if user:
            user_name = f"{user['first_name']} {user['last_name']}"

    return render_template("index.html", name=user_name, city=city, temp=temp)

