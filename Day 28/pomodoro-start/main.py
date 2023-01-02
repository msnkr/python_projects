from tkinter import *
from PIL import ImageTk, Image
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Hack"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = ImageTk.PhotoImage(Image.open('Day 28/pomodoro-start/tomato.png'))
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)

timer_label = Label()
timer_label.config(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, '45', 'bold'))
timer_label.grid(column=2, row=1)

start_button = Button()
start_button.config(text='Start')
start_button.grid(column=1, row=3)

reset_button = Button()
reset_button.config(text='reset')
reset_button.grid(column=3, row=3)

checkmark_label = Label()
checkmark_label.config(text='✔', bg=YELLOW, fg=GREEN, font=('Hack', 20))
checkmark_label.grid(column=2, row=3)

window.mainloop()