from tkinter import *
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ('Arial', 40, 'italic')
FONT2 = ('Arial', 60, 'bold')


window = Tk()
window.title('Flashy')
window.config()

canvas = Canvas(width=1200, height=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = ImageTk.PhotoImage(Image.open('Day 31/flash-card-project-start/images/card_front.png'))
canvas.create_image(800, 526, image=canvas_img)
canvas.grid(column=0, row=0)


# Buttons
x_button_img = ImageTk.PhotoImage(Image.open('Day 31/flash-card-project-start/images/wrong.png'))
x_button = Button(image=x_button_img, highlightthickness=0)
x_button.grid(column=0, row=1)

right_button_img = ImageTk.PhotoImage(Image.open('Day 31/flash-card-project-start/images/right.png'))
right_button = Button(image=right_button_img, highlightthickness=0)
right_button.grid(column=1, row=1)


window.mainloop()

