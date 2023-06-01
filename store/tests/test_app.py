from app import app


app.testing = True
client = app.test_client()


def test_index():
    response = client.get("/")
    assert b"Today's temperature in" in response.data


def test_login():
    response = client.get("/login?error='test error message'")
    assert b"test error message" in response.data
    assert b"Email:" in response.data
    assert b"Password:" in response.data


def test_signup():
    response = client.get("/signup")
    assert b"Email:" in response.data
    assert b"First name:" in response.data
    assert b"Last name:" in response.data
    assert b"Password:" in response.data


def test_cart():
    response = client.get("/viewcart")
    assert b"You should be redirected automatically to the target URL" in response.data
    assert b'<a href="/login">/login</a>' in response.data
