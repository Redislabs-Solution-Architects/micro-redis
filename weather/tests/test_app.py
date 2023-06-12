import unittest

from app import app

app.testing = True
client = app.test_client()


class TestWeather(unittest.TestCase):
    def test_index(self):
        response = client.get("/")
        assert b"Index" in response.data

    def test_get_weather(self):
        response = client.get("/get_weather/xyz")
        assert b'{"cod":401,"message":"Invalid API key.' in response.data
