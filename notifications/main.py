from tkinter import *
from datetime import datetime
from plyer import notification


def start():
    task = task_name_entry.get()
    total_time = int(time_entry.get())

    seconds = (total_time * 60) * 60
    



window = Tk()
window.title("Task Manager")
window.config(width=400, height=400, padx=10, pady=10)

task_name_label = Label(window, text="What task do you want to be notified for? ")
task_name_label.grid(column=0, row=0)

task_name_entry = Entry(window)
task_name_entry.grid(column=0, row=1)

time_label = Label(window, text="How many hours? ")
time_label.grid(column=0, row=2)

time_entry = Entry(window)
time_entry.grid(column=0, row=3)

start_btn = Button(window, text="Start", command=start)
start_btn.grid(column=0, row=4)

quit_btn = Button(window, text="Quit", command=window.destroy)
quit_btn.grid(column=1, row=4)


window.mainloop()



# title = "This is a title"
# message = "This is a message"


# notification.notify(title, message, toast=True, timeout=3)
