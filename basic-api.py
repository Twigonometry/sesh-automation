import conf_secret
import requests

base_url = "http://api.openweathermap.org/data/2.5/forecast"

parameters = {'q':'Sheffield,UK','appid':conf_secret.openweather_key}

response = requests.get(base_url, params=parameters)

print(response.content)