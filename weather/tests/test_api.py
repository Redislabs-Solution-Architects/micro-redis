import unittest

from app.utility import get_weather_endpoint


class TestWeather(unittest.TestCase):
    def test_get_weather_endpoint(self):
        url = get_weather_endpoint("ann arbor")
        assert url == "https://api.openweathermap.org/data/2.5/weather?q=ann+arbor&units=imperial&appid=foo"