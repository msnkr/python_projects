from turtle import Turtle


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.setposition(x=0, y=380)
        self.color('white')
        self.SCORE = 0
        self.write(arg=f'Score: {self.SCORE}', align='center', font=('Arial', 12, 'normal'))



    
    def add_score(self):
        self.clear()
        self.SCORE += 1
        self.write(arg=f'Score: {self.SCORE}', align='center', font=('Arial', 12, 'normal'))

