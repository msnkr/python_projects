from turtle import Turtle


FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.current_level()


    def current_level(self):
        self.clear()
        self.goto(-300, 300)
        self.write(f'Level: {self.level}', align='center', font=FONT)


    def level_up(self):
        self.level += 1
        self.current_level()


    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)

        