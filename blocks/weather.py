import requests
import json

url = "https://api.weatherbit.io/v2.0/forecast/daily "

def say(CONFIG):

    response = requests.request("GET", url, params=CONFIG['weather'])
    weather = json.loads(response.text)["data"][0]

    return f"Mai időjárás: {weather['temp']} fok, {weather['weather']['description']}. "
