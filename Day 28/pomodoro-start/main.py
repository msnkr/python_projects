from tkinter import *
import math
from PIL import ImageTk, Image
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Source Code Pro"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def start_timer():
    count_down(5)

# ---------------------------- UI SETUP ------------------------------- #

def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = ImageTk.PhotoImage(Image.open('Day 28/pomodoro-start/tomato.png'))
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, '45', 'bold'))
timer_label.grid(column=2, row=1)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text='reset', highlightthickness=0)
reset_button.grid(column=3, row=3)

checkmark_label = Label(text='✔', bg=YELLOW, fg=GREEN, font=('Hack', 20))
checkmark_label.grid(column=2, row=3)

window.mainloop()