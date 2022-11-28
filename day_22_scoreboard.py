from turtle import Turtle


FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = 0


    def current_level(self):
        self.goto(-300, 300)
        self.write(f'Level {self.level}', align='center', font=FONT)


    def rewrite_level(self):
        self.clear()
        self.level += 1
        self.current_level()

    
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)

