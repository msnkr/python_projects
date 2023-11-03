import math
from tkinter import *
import requests


key = "888fc6acf8d5a7a7b9e51209de4178cc"
req = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?q=Johannesburg,ZA&appid={}".format(key))

if req.ok:
    response = req.json()

    temp, weather_description = math.floor(
        response["main"]["temp"] / 10), response["weather"][0]["main"]
    icon_bitmap = response['weather'][0]['icon']
    icon = f"https://openweathermap.org/img/wn/{icon_bitmap}@2x.png"


window = Tk()


window.title("Weather API")
window.geometry("600x400")


country_label = Label(window, text="Weather for Johannesburg")
country_label.pack()
country_label.config(font=("Arial", 22, "bold"))


weather_label = Label(window, text="{}C".format(temp))
weather_label.pack()

description_label = Label(window, text=weather_description)
description_label.pack()

canvas = Canvas(window, width=300, height=200, background="white")
canvas.pack()

image = PhotoImage(icon)
canvas.create_image(100, 100, image)

window.mainloop()
