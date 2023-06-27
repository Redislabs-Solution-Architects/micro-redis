import unittest
from unittest.mock import patch

from app.utility import redis_conn
from app.weather import get_weather


class TestWeather(unittest.TestCase):
    def test_get_weather_bad_key(self):
        redis_conn.json().delete("weather:Atlantis")
        the_weather = get_weather("Atlantis")
        assert the_weather["cod"] == 401
        key = redis_conn.json().get("weather:Atlantis")
        self.assertIsNone(key)

    @patch("requests.get")
    def test_get_weather_mocked(self, mock_get):
        redis_conn.json().delete("weather:Rivendell")
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"cod": 200, "name": "Rivendell"}

        the_weather = get_weather("Rivendell")
        first_time = the_weather["total_time"]
        self.assertEqual("Rivendell", the_weather["name"])
        self.assertLess(0, first_time)

        the_weather = get_weather("Rivendell")
        self.assertEqual("Rivendell", the_weather["name"])
        self.assertLess(0, the_weather["total_time"])
        redis_conn.json().delete("weather:Rivendell")
