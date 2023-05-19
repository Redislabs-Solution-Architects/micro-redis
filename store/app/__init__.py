from flask import Flask
from flask import render_template, request

from app.controllers import signup_controller, login_controller, cart_controller, home_controller

app = Flask(__name__)


@app.route("/")
def home():
    return home_controller.show_home(request)


@app.route("/login")
def show_login():
    return login_controller.show_login(request)


@app.route("/logout")
def logout():
    return login_controller.logout_user()


@app.route("/loginuser", methods=["POST"])
def login_user():
    return login_controller.login_user(request)


@app.route("/signup")
def show_signup():
    return signup_controller.show_signup()


@app.route("/signupuser", methods=["POST"])
def signup_user():
    return signup_controller.signup_user(request)


@app.route("/viewcart", methods=["GET", "POST"])
def view_cart():
    return cart_controller.view_cart(request, None)


@app.route("/updatecart", methods=["POST"])
def update_cart():
    return cart_controller.update_cart(request)
