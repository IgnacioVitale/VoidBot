import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

# https://openweathermap.org/api/geocoding-api
url = f"http://api.openweathermap.org/geo/1.0/direct?q=London&limit=1&appid={os.getenv('OPENWEATHER_API_KEY')}"


# ☀️🌤️⛅🌥️☁️🌦️🌧️⛈️🌩️🌨️❄️

def get_geo_info(city):
    # https://openweathermap.org/api/geocoding-api
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city.capitalize()}" \
              f"&limit=1&appid={os.getenv('OPENWEATHER_API_KEY')}"
    req = requests.get(geo_url, json=None)
    content = json.loads(req.text)
    # Maybe there is a cleaner way to do this? If we get no content, we return none
    if not content:
        return None, None, None
    content = content[0]
    lat = content['lat']
    lon = content['lon']
    # We attatch the country initials to the city
    city_name = f"{content['name']}, {content['country']}"
    return lat, lon, city_name


def get_weather(city):
    # We get the latitude and longitude of the city
    lat, lon, city_name = get_geo_info(city)
    # If the city is nt found, we throw an error
    if not city_name:
        return f"The city has not been found", None
    # with the lat and lon, we can get the weather info
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?" \
                  f"lat={lat}&lon={lon}&appid={os.getenv('OPENWEATHER_API_KEY')}&units=metric"
    req = requests.get(weather_url, json=None)
    content = json.loads(req.text)
    # We get the icon to add a reaction
    icon = get_icon(content['weather'][0])
    weather = content['weather'][0]['main']
    temp = content['main']['temp']
    message = f"The weather in {city_name} is : {temp}°, {weather}."
    return message, icon


def get_icon(weather):
    icons = {
        'broken clouds': '🌥️',
        'scattered clouds': '☁️',
        'shower rain': '🌧️',
    }
    icons_basic = {
        'clear': '☀️',
        'clouds': '☁️',
        'snow': '❄️',
        'rain': '🌧️',
        'drizzle': '🌦️',
        'thunderstorm': '⛈️'

    }
    if weather['description'].lower() in icons:
        return icons[weather['description'].lower()]
    if weather['main'].lower() in icons_basic:
        return icons_basic[weather['main'].lower()]
    return None
