from tkinter import *
import faker


fake = faker.Faker()


def word_list():
    return " ".join([fake.word().lower() for _ in range(30)])


window = Tk()


window.title("Eggghh")
window.config(bg="grey", padx=20, pady=20)


timer = Label(window, text="00")
timer.grid(row=0, column=1)
timer.config(bg="grey", font=("Arial", 22, "bold"))

canvas_words = Canvas(window, width=300, height=200)
canvas_words.grid(row=1, column=0)

canvas_text = Text(canvas_words, width=40, height=10, padx=20, pady=20)
canvas_text.grid(row=1, column=0)
canvas_text.insert(END, word_list())


start_btn = Button(window, text="Start")
start_btn.grid(row=1, column=1)
start_btn.config(padx=5)


canvas_type = Canvas(window, width=300, height=200)
canvas_type.grid(row=1, column=2)

canvas_type = Text(canvas_type, width=40, height=10, padx=20, pady=20)
canvas_type.grid(row=1, column=0)
canvas_type.insert(END, "")

window.mainloop()


# Press start button should start the timer, should bring up the text to type also
