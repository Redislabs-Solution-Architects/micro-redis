from utility import get_weather_endpoint


def test_get_weather_endpoint():
    url = get_weather_endpoint("ann arbor")
    assert url == "https://api.openweathermap.org/data/2.5/weather?q=ann+arbor&units=imperial&appid=None"