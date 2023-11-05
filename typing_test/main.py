from tkinter import *
import math
import faker


fake = faker.Faker()


def get_text():
    words = text_to_copy
    typed_words = canvas_type.get("1.0", "end")

    total_chars = 0
    for word in words.split():
        for typed_word in typed_words.split():
            if word == typed_word:
                total_chars += len(typed_word)

    wpm_text.config(text=math.floor(total_chars / 5))


def countdown_timer(count):
    count -= 1
    timer_seconds = window.after(1000, countdown_timer, count)
    timer.config(text=count)

    if count == 0:
        window.after_cancel(timer_seconds)
        canvas_type.configure(state=DISABLED)
        get_text()


def start():
    canvas_text.insert(END, text_to_copy)
    countdown_timer(30)


def word_list():
    return " ".join([fake.word().lower() for _ in range(30)])


text_to_copy = word_list()


window = Tk()


window.title("Eggghh")
window.config(bg="darkgrey", padx=20, pady=20)


timer = Label(window, text="30")
timer.grid(row=0, column=1)
timer.config(bg="darkgrey", font=("Arial", 22, "bold"))

canvas_words = Canvas(window, width=300, height=200)
canvas_words.grid(row=1, column=0)

canvas_text = Text(canvas_words, width=40, height=10, padx=20, pady=20)
canvas_text.grid(row=1, column=0)


start_btn = Button(window, text="Start", command=start)
start_btn.grid(row=1, column=1)
start_btn.config(padx=5)


canvas_type = Canvas(window, width=300, height=200)
canvas_type.grid(row=1, column=2)

canvas_type = Text(canvas_type, width=40, height=10, padx=20, pady=20)
canvas_type.grid(row=1, column=0)
canvas_type.insert(END, "")

wpm_text = Label(window, text=0)
wpm_text.grid(row=2, column=1)
wpm_text.config(bg="darkgrey", font=("Arial", 22, "bold"))


window.mainloop()
