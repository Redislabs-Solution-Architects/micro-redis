import hashlib

from flask import render_template, make_response, redirect

from app.utility import redis_conn


def show_signup():
    action_url = "/signupuser"
    return render_template("signup.html", action_url=action_url)


def signup_user(request):
    password = request.form.get("password")
    user = dict(
        first_name=request.form.get("firstname"),
        last_name=request.form.get("lastname"),
        email=request.form.get("email"),
        password=hashlib.md5(password.encode()).hexdigest()
    )

    redis_conn.json().set(f"users:{user['email']}", "$", user)

    print(f"signup_user email: {user['email']}")
    resp = make_response(redirect("/login"))
    return resp
