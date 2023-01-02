from tkinter import *

window = Tk()
window.title('Miles to KM converter')
window.config(padx=150, pady=150)

# 3 Rows and 3 columns
# Create a calculate button
# Caluculate function must get() data input, * input by 1.6 and change label to answer


def calculate():
    calculate_km = int(data_entry.get()) * 1.6
    item.config(text=round(calculate_km))


data_entry = Entry()
data_entry.grid(column=2, row=0)

miles_label = Label(text='Miles', font=('Hack', 16, 'bold'))
miles_label.grid(column=3, row=0)

equal_to = Label(text='Is equal to', font=('Hack', 16))
equal_to.grid(column=1, row=1)

item = Label(text='0', font=('Hack', 16))
item.grid(column=2, row=1)

km_label = Label(text='km', font=('Hack', 16, 'bold'))
km_label.grid(column=3, row=1)

button = Button(text='Button', command=calculate)
button.grid(column=2, row=2)




window.mainloop()