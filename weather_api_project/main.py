import math
from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

key = "888fc6acf8d5a7a7b9e51209de4178cc"
req = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?q=Johannesburg,ZA&appid={}".format(key))

if req.ok:
    response = req.json()

    temp, weather_description = math.floor(
        response["main"]["temp"] / 10), response["weather"][0]["main"]


window = Tk()
window.config(padx=10, pady=30)

window.title("Weather API")
window.geometry("600x200")


country_label = Label(window, text="Weather for Johannesburg")
country_label.pack()
country_label.config(font=("Arial", 22, "bold"))


weather_label = Label(window, text="{}C".format(temp))
weather_label.pack()
weather_label.config(font=("Arial", 22, "bold"))

description_label = Label(window, text=weather_description)
description_label.pack()
description_label.config(font=("Arial", 22, "bold"))

window.mainloop()
