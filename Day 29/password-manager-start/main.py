from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint, choice, shuffle
import pyperclip


WHITE = 'white'
FONT = ('Iosveka', 12, 'bold')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = ''.join(password_list)
    
    pyperclip.copy(password)
    password_entry.insert(0, password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web_data = website_entry.get()
    username_data = email_username_entry.get()
    password_data = password_entry.get()

    if len(web_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title='One of your fields are empty.', message='Don\'t leave any empty fields.')
    else:
        clicked_yes = messagebox.askyesno(title='Save this password?:', message=f'Save these details?: \n {web_data} \n {username_data} \n {password_data}')
        if clicked_yes:
            with open('Day 29/password-manager-start/data.txt', 'a')as data:
                data.write(f'{web_data} | {username_data} | {password_data} \n')  
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title('Password Manger')
window.config(padx=50, pady=50, bg=WHITE)

# Canvas
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
canvas_img = ImageTk.PhotoImage(Image.open('Day 29/password-manager-start/logo.png'))
canvas.create_image(100, 100, image=canvas_img)
canvas.grid(column=1, row=1)


# Labels
website = Label(text='Website: ', bg=WHITE, font=FONT)
website.grid(column=0, row=2)

email_username = Label(text='Email/Username: ', bg=WHITE, font=FONT)
email_username.grid(column=0, row=3)

password = Label(text='Password', bg=WHITE, font=FONT)
password.grid(column=0, row=4)

# Entry
website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=2, columnspan=3, sticky='EW')

email_username_entry = Entry()
email_username_entry.insert(0, 'RandomEmail@gmail.com')
email_username_entry.grid(column=1, row=3, columnspan=3, sticky='EW')

password_entry = Entry()
password_entry.grid(column=1, row=4, sticky='EW')

# Button
generate_pass_button = Button(text='Generate Password', bg=WHITE, font=('Iosveka', 8), command=generate_password)
generate_pass_button.grid(column=2, row=4, sticky='EW')

add_button = Button(text='Add', bg=WHITE, font=('Iosveka', 8), width=36, command=save)
add_button.grid(column=1, row=5, columnspan=4, sticky='EW')

window.mainloop()