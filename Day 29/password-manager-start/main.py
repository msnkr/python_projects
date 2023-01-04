from tkinter import *
from PIL import Image, ImageTk

WHITE = 'white'
FONT = ('Iosveka', 12, 'bold')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title('Password Manger')
window.config(padx=20, pady=20, bg=WHITE)

# Canvas
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
canvas_img = ImageTk.PhotoImage(Image.open('Day 29/password-manager-start/logo.png'))
canvas.create_image(100, 100, image=canvas_img)
canvas.grid(column=2, row=1)


# Labels
website = Label(text='Website: ', bg=WHITE, font=FONT)
website.grid(column=1, row=2)

email_username = Label(text='Email/Username: ', bg=WHITE, font=FONT)
email_username.grid(column=1, row=3)

password = Label(text='Password', bg=WHITE, font=FONT)
password.grid(column=1, row=4)

# Entry
website_entry = Entry()
website_entry.grid(column=2, row=2, columnspan=3)

email_username_entry = Entry()
email_username_entry.grid(column=2, row=3, columnspan=3)

password_entry = Entry()
password_entry.grid(column=2, row=4)

# Button
generate_pass_button = Button(text='Generate', bg=WHITE, font=('Iosveka', 8))
generate_pass_button.grid(column=3, row=4)



window.mainloop()