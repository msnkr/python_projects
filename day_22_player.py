from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.FINISH_LINE_Y = 280
        self.move_increment = 0.1


    def move_up(self):
        self.forward(MOVE_DISTANCE)
    

    def increase_level(self):
        self.goto(STARTING_POSITION)
        self.move_increment *= 0.9