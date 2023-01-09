from tkinter import *
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ('Arial', 40, 'italic')
FONT2 = ('Arial', 60, 'bold')


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=1000, height=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_img = ImageTk.PhotoImage(Image.open('Day 31/flash-card-project-start/images/card_front.png'))
canvas.create_image(550, 400, image=canvas_img)

# Canvas Text
french_word = canvas.create_text(550, 250, text='French', font=FONT1)
french = canvas.create_text(550, 450, text='Word', font=FONT2)
canvas.grid(column=1, row=1)


# Buttons
wrong_button_img = ImageTk.PhotoImage(Image.open('Day 31/flash-card-project-start/images/wrong.png'))
wrong_button = Button(image=wrong_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, padx=5, pady=5)
wrong_button.grid(column=1, row=2)

right_button_img = ImageTk.PhotoImage(Image.open('Day 31/flash-card-project-start/images/right.png'))
right_button = Button(image=right_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, padx=5, pady=5)
right_button.grid(column=2, row=2)


window.mainloop()

