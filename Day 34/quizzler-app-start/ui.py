from tkinter import *
from tkinter import PhotoImage
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")

        self.window.config(background=THEME_COLOR, padx=20, pady=10)
        self.window.grid()

        self.score_label = Label(self.window, text="Score: 0")
        self.score_label.config(background=THEME_COLOR, foreground="white")
        self.score_label.grid(column=1,  row=0)

        self.second_window = Canvas(
            self.window, width=300, height=250, background="white")
        question_text = self.second_window.create_text(150, 125,
                                                       text="Some question text", fill=THEME_COLOR, font=("Arial", 16, "italic"))
        self.second_window.grid(
            row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(
            file=r"C:\Users\mikyl\Documents\Git\python_projects\Day 34\quizzler-app-start\images\true.png")
        false_img = PhotoImage(
            file=r"C:\Users\mikyl\Documents\Git\python_projects\Day 34\quizzler-app-start\images\false.png")

        self.true_btn = Button(
            self.window, image=true_img, command=None, highlightthickness=0, highlightcolor=None)
        self.true_btn.grid(row=2, column=0)
        self.false_btn = Button(
            self.window, image=false_img, command=None, highlightthickness=0, highlightcolor=None)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

        def get_next_question(self):
            q_text = self.quiz.next_question()
            self.second_window.itemconfig(
                self.q_text, text=question_text)
