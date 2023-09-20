from tkinter import *
from PIL import Image, ImageTk
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    json_response = response.json()
    canvas.itemconfig(quote_text, text=json_response["quote"])


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)


canvas = Canvas(width=300, height=414)
background_img = PhotoImage(
    file=r"Day 33/kanye-quotes-start/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Text goes here", width=250, font=(
    "Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(
    file=r"C:\Users\mikyl\Documents\Git\python_projects\Day 33\kanye-quotes-start\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
