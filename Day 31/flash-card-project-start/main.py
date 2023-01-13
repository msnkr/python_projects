from tkinter import *
from PIL import Image, ImageTk
import pandas
from random import choice


################## RANDOM DATA #####################

pd = pandas.read_csv('Day 31/flash-card-project-start/data/french_words.csv')

word = choice(pd.French)
english_word = 


################## CANVAS #####################

# BACKGROUND_COLOR = "#B1DDC6"
# FONT1 = ('Arial', 40, 'italic')
# FONT2 = ('Arial', 60, 'bold')


# window = Tk()
# window.title('Flashy')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
# canvas_img = ImageTk.PhotoImage(Image.open('Day 31/flash-card-project-start/images/card_front.png'))
# canvas.create_image(400, 263, image=canvas_img)

# # Canvas Text
# canvas.create_text(400, 150, text='Title', font=FONT1)
# canvas.create_text(400, 263, text='Word', font=FONT2)
# canvas.grid(column=0, row=0, columnspan=2)

# # Buttons
# wrong_button_img = ImageTk.PhotoImage(Image.open('Day 31/flash-card-project-start/images/wrong.png'))
# wrong_button = Button(image=wrong_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, padx=5, pady=5)
# wrong_button.grid(column=0, row=1)

# right_button_img = ImageTk.PhotoImage(Image.open('Day 31/flash-card-project-start/images/right.png'))
# right_button = Button(image=right_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, padx=5, pady=5)
# right_button.grid(column=1, row=1)

# window.mainloop()
