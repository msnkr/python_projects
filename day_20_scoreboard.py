from turtle import Turtle


SCORE = 0
class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.setposition(x=0, y=380)
        self.color('white')

    
    def add_score(self):
        global SCORE
        self.clear()
        SCORE += 1
        self.write(arg=f'Score: {SCORE}', align='center', font=('Arial', 12, 'normal'))
