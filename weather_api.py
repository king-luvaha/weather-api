import requests
import os

API_KEY = os.getenv("API_KEY")

def get_weather(city):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={API_KEY}&contentType=json"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Error fetching weather data")

    return response.json()
