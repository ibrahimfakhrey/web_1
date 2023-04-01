
import requests

END_POINT="https://api.openweathermap.org/data/2.5/weather"
API="868c5469fc5add3122d3e7e8313c8f3e"
params={
    "lat":"40.712776",
    "lon":"-74.005974",
    "appid":API
}

response=requests.get(url=END_POINT,params=params)
weather_data=response.json()
temp_inc=weather_data["main"]["temp"]
temp=int(temp_inc)-273
print(temp)