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
        self.second_window.grid(
            row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(
            file=r"C:\Users\mikyl\Documents\Git\python_projects\Day 34\quizzler-app-start\images\true.png")
        false_img = PhotoImage(
            file=r"C:\Users\mikyl\Documents\Git\python_projects\Day 34\quizzler-app-start\images\false.png")

        self.true_btn = Button(
            self.window, image=true_img, command=self.check_answer_true, highlightthickness=0, highlightcolor=None)
        self.true_btn.grid(row=2, column=0)
        self.false_btn = Button(
            self.window, image=false_img, command=self.check_answser_false, highlightthickness=0, highlightcolor=None)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.q_text = self.quiz.next_question()
        self.second_window.config(bg="white")
        self.second_window.create_text(
            150, 125, text=self.q_text, fill=THEME_COLOR, font=("Arial", 16, "italic"), width=280)

    def check_answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_answser_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.second_window.config(bg="white")
        self.quiz.next_question()

    def give_feedback(self, is_right):
        self.second_window.after(1000, self.change_color(is_right))
        self.get_next_question()

    def change_color(self, stat):
        if stat == True:
            self.second_window.config(bg="green")
        elif stat == False:
            self.second_window.config(bg="red")
