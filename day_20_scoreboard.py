from turtle import Turtle


ALIGNMENT = 'center'
FONT = ('Hack', 22, 'normal')

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.setposition(x=0, y=420)
        self.color('white')
        self.SCORE = 0
        self.update_score()


    def update_score(self):
        self.write(arg=f'Score: {self.SCORE}', align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.setposition(x=0, y=0)
        self.write(arg=f'GAME OVER: {self.SCORE}', align=ALIGNMENT, font=FONT)

    
    def add_score(self):
        self.clear()
        self.SCORE += 1
        self.update_score()

