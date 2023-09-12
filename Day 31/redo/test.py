from tkinter import *
from tkinter import ttk


root = Tk()

root.title("Hello")
frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True, padx=8, pady=8)


def hello_text():
    print("Hello World")


ttk.Label(frame, text="Hello, World!").pack(fill="both")
ttk.Button(frame, text="Click Here", command=hello_text).pack(fill="both")
ttk.Button(frame, text="Quit", command=root.destroy).pack(fill="both")


root.mainloop()
