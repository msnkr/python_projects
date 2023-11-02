import math
import requests


key = "888fc6acf8d5a7a7b9e51209de4178cc"

url = f"https://api.openweathermap.org/data/2.5/weather?q=Johannesburg,ZA&appid={key}"

req = requests.get(url)

if req.ok:
    response = req.json()
    
    temp = math.floor(response["main"]["temp"] / 10)
    weather_description = response["weather"][0]["main"]


print("{}. The temp is {}°C ".format(weather_description, temp))
