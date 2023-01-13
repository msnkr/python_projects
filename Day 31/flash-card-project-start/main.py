from tkinter import *
from PIL import Image, ImageTk
import pandas
from random import choice


################## BACK OF THE CARD #####################

def back_card(english_word):
   canvas.itemconfig(canvas_image, image=back_image)
   canvas.itemconfigure(card_title, text='English', fill='white')
   canvas.itemconfigure(card_word, text=english_word, fill='white')
   canvas.after_cancel(x)

################## RANDOM DATA #####################

def generate_card():
    current_card = choice(new_dict)
    canvas.itemconfigure(card_title, text='French')
    canvas.itemconfigure(card_word, text=current_card['French'])
    english_word = current_card['English']
    canvas.after(3000, back_card, english_word)


pd = pandas.read_csv('Day 31/flash-card-project-start/data/french_words.csv')
new_dict = pd.to_dict(orient='records')

################## CANVAS #####################

BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ('Arial', 40, 'italic')
FONT2 = ('Arial', 60, 'bold')


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_img = ImageTk.PhotoImage(Image.open('Day 31/flash-card-project-start/images/card_front.png'))
canvas_image = canvas.create_image(400, 263, image=canvas_img)
back_image = ImageTk.PhotoImage(Image.open('Day 31/flash-card-project-start/images/card_back.png'))


# Canvas Text
card_title = canvas.create_text(400, 150, text='', font=FONT1)
card_word = canvas.create_text(400, 263, text='', font=FONT2)
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
wrong_button_img = ImageTk.PhotoImage(Image.open('Day 31/flash-card-project-start/images/wrong.png'))
wrong_button = Button(image=wrong_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, padx=5, pady=5, command=generate_card)
wrong_button.grid(column=0, row=1)

right_button_img = ImageTk.PhotoImage(Image.open('Day 31/flash-card-project-start/images/right.png'))
right_button = Button(image=right_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, padx=5, pady=5, command=generate_card)
right_button.grid(column=1, row=1)

generate_card()

window.mainloop()
