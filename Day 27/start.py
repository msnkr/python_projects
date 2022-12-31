from tkinter import *
import time

window = Tk()

window.title('Gui')
# my_label = Label(text='This is a label.', font=('Hack', 24))
# # You can set options using the set command.
# # my_label.config(text='New Text')
# # Or
# # my_label['text'] = 'This is new text'

# my_label.pack()

# # Eveent listeners
# def button_clicked():
#     my_label.config(text='I got clicked')

# # Buttons
# new_button = Button()
# new_button.config(bg='teal', fg='white', text='Hello. I\'m a button', command=button_clicked)
# new_button.pack()

# # Data entry
# user_entry = Entry(width=10)
# user_entry.pack()

def listen_for_button():
    """
    Change label
    """
    new_label.config(text=f'{text_data.get()}')


# Label
new_label = Label(text='This is a label.', font=('Hack', 22))
new_label.pack()

# Data
text_data = Entry(width=25)
text_data
text_data.pack()

# Button
button = Button(text='Click me to change the label', font=('Hack', 16), fg='white', bg='black', command=listen_for_button)
button.pack()

window.mainloop()

