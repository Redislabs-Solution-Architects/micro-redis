import unittest
from unittest.mock import patch

from app import weather


class TestWeather(unittest.TestCase):
    def test_get_weather_bad_key(self):
        the_weather = weather.get_weather("Springfield")
        assert the_weather["cod"] == 401

    @patch("requests.get")
    def test_get_weather_mocked(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"cod": 200, "name": "Denver"}

        the_weather = weather.get_weather("Denver")
        first_time = the_weather["total_time"]
        self.assertEqual("Denver", the_weather["name"])
        self.assertLess(0, first_time)

        the_weather = weather.get_weather("Denver")
        self.assertEqual("Denver", the_weather["name"])
        self.assertLess(0, the_weather["total_time"])
