from tkinter import *
import time

window = Tk()

window.title('Gui')
my_label = Label(text='This is a label.', font=('Hack', 24))
# You can set options using the set command.
# my_label.config(text='New Text')
# Or
# my_label['text'] = 'This is new text'

my_label.pack()

# Eveent listeners
def button_clicked():
    my_label.config(text='I got clicked')

# Buttons
new_button = Button()
new_button.config(bg='teal', fg='white', text='Hello. I\'m a button', command=button_clicked)
new_button.pack()

# Data entry
user_entry = Entry()
user_input = user_entry.get()
user_entry.pack()



window.mainloop()
