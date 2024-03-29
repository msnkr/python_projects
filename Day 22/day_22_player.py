from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.finish_line()
        self.FINISH_LINE_Y = 280


    def move_up(self):
        self.forward(MOVE_DISTANCE)

    
    def finish_line(self):
        self.goto(STARTING_POSITION )

    