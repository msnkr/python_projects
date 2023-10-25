from tkinter import *
import math
from plyer import notification

def send_fifteen(seconds):
    notification.notify(title=f"{task_name_entry.get()}", message="You have 15 minutes left")


def send_notification(seconds):
    notification.notify(title=f"{task_name_entry.get()}", message=f"Your time is {math.floor(seconds / 60 )} minutes. ")


def count_seconds(seconds):  

    task_seconds_label = Label(frame, text=f"{math.floor(seconds / 60)}:{seconds % 60}")
    task_seconds_label.grid(column=2, row=0, padx=20, pady=2)
    task_seconds_label.config(bg="white")
    seconds -= 1
    frame.after(1000, count_seconds, seconds)   

    if seconds == 900:
        send_fifteen(seconds)


def add_task():
    task = task_name_entry.get()
    seconds = (int(time_entry.get()) * 60) * 60

    add_task_label = Label(frame, text=task)
    add_task_label.grid(column=0, columnspan=2, row=0, padx=20, pady=2)
    add_task_label.config(bg="white")
    
    count_seconds(seconds)
    send_notification(seconds)




window = Tk()
window.title("Task Manager")
window.config(padx=10, pady=10)

task_name_label = Label(window, text="What task do you want to be notified for? ")
task_name_label.grid(column=0, columnspan=2, row=0, padx=2, pady=2)

task_name_entry = Entry(window)
task_name_entry.grid(column=0, columnspan=2, row=1, padx=2, pady=2)

time_label = Label(window, text="How many hours? ")
time_label.grid(column=0, columnspan=2, row=2, padx=2, pady=2)

time_entry = Entry(window)
time_entry.grid(column=0, columnspan=2, row=3, padx=2, pady=2)

start_btn = Button(window, text="Start", command=add_task)
start_btn.grid(column=0, row=4, padx=2, pady=2)

quit_btn = Button(window, text="Quit", command=window.destroy)
quit_btn.grid(column=1, row=4, padx=2, pady=2)


frame = Frame(background="white", padx=10, pady=10)
frame.config(width=200, height=200, padx=2, pady=2)
frame.grid(column=0, columnspan=2, row=5, padx=2, pady=2)


window.mainloop()
