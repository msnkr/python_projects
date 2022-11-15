from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-150, 300)
        self.write(self.left_score, align='center', font=('Hack', 24, 'normal'))
        self.goto(150, 300)
        self.write(self.right_score, align='center', font=('Hack', 24, 'normal'))


    def left_point(self):
        self.left_score += 1
        self.update_score()

    
    def right_point(self):
        self.right_score += 1
        self.update_score()