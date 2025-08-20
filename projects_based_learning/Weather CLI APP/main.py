import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("WEATHER_API_KEY")


def _make_request(city:str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def get_info(data):
    result = {
    "id" : data["id"],
    "temp" : data["main"]["temp"],
    "humidity" : data["main"]["humidity"]
    }
    return result

print(get_info(_make_request('Paris')))