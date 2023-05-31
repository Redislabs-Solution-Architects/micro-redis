from app import app

app.testing = True
client = app.test_client()


def test_index():
    response = client.get("/")
    assert b"Index" in response.data


def test_get_weather():
    response = client.get("/get_weather/xyz")
    assert b'{"Code":401,"Error":"Calling weather endpoint failed","Message":"Unauthorized"}\n' in response.data