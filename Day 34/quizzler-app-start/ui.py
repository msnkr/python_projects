from tkinter import *
from tkinter import PhotoImage


THEME_COLOR = "#375362"


class QuizInterface():

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizler")

        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.window.grid()

        score_label = Label(self.window, text="Score: 0")
        score_label.config(background=THEME_COLOR, foreground="white")
        score_label.grid(column=1, columnspan=2,  row=0)

        second_window = Frame(self.window)
        second_window.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        second_window.config(width=300, height=250)

        # question = Label(
        #     second_window, text="This is a question", background="white", padx=10, pady=10)
        # question.grid(column=0, row=0)

        true_img = PhotoImage(
            file=r"C:\Users\mikyl\Documents\Git\python_projects\Day 34\quizzler-app-start\images\true.png")
        false_img = PhotoImage(
            file=r"C:\Users\mikyl\Documents\Git\python_projects\Day 34\quizzler-app-start\images\false.png")

        true_btn = Button(self.window, image=true_img, command=None)
        true_btn.grid(row=2, column=0)
        false_btn = Button(self.window, image=false_img, command=None)
        false_btn.grid(row=2, column=1)

        self.window.mainloop()
