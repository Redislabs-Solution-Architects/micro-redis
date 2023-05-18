import hashlib

from flask import render_template, make_response, redirect

from app.utility import redis_conn, session


def show_login(request):
    action_url = "/loginuser"
    return render_template("login.html", action_url=action_url, error=request.args.get("error"))


def login_user(request):
    email = request.form.get("email")
    password = request.form.get("password")

    # Validate credentials
    user = redis_conn.json().get(f"users:{email}")
    pass_hash = hashlib.md5(password.encode()).hexdigest()
    if pass_hash != user["password"]:
        resp = make_response(redirect("/login?error=Invalid+credentials"))
        return resp

    # Create a session
    session_id = session.create_session(email)

    resp = make_response(redirect("/viewcart"))
    resp.set_cookie(
        key="storesessionid",
        value=session_id,
        httponly=True,
    )
    return resp


def logout_user():
    resp = make_response(render_template("index.html"))
    resp.delete_cookie("storesessionid")
    return resp
