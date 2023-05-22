import hashlib

from flask import render_template, make_response, redirect

from app.utility import redis_conn


def show_signup(request):
    action_url = "/signupuser"
    return render_template("signup.html", action_url=action_url, error=request.args.get("error_msg"))


def signup_user(request):
    password = request.form.get("password")
    email = request.form.get("email")

    user = redis_conn.json().get(f"users:{email}")
    if user:
        error_msg = "That email is already in use."
        resp = make_response(redirect(f"/signup?error_msg={error_msg}"))
        return resp

    user = dict(
        first_name=request.form.get("firstname"),
        last_name=request.form.get("lastname"),
        email=email,
        password=hashlib.md5(password.encode()).hexdigest()
    )

    redis_conn.json().set(f"users:{user['email']}", "$", user)

    print(f"signup_user email: {user['email']}")
    resp = make_response(redirect("/login"))
    return resp
