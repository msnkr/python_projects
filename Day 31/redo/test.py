from tkinter import *
from tkinter import ttk
from tkinter import colorchooser


root = Tk()

root.title("Hello")
frame = ttk.Frame(root, padding=20)
frame.grid()


def hello_text():
    print("Hello World")


ttk.Label(frame, text="Hello, World!").grid(column=0, row=0)
ttk.Button(frame, text="Click Here", command=hello_text).grid(column=0, row=1)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=1)


root.mainloop()
