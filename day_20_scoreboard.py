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
        # self.high_score = self.read_highscore()
        with open('day_24_data.txt')as file:
            self.high_score = int(file.read())
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(arg=f'Score: {self.SCORE}. High score: {self.high_score}', align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.SCORE > self.high_score:
            self.high_score = self.SCORE
            with open('day_24_data.txt', 'w')as file:
                file.write(f'{self.high_score}')
        self.SCORE = 0
        self.update_score()


    def add_score(self):
        self.clear()
        self.SCORE += 1
        self.update_score()


    # def read_highscore(self):
    #     """Read the highscore from data.txt"""
    #     with open('day_24_data.txt')as file:
    #         return int(file.read())


    # def write_highscore(self, new_score):
    #     """Write a new highscore if it\'s bigger than current score"""
    #     with open('day_24_data.txt', 'w')as file:
    #         file.write(str(new_score))