from turtle import Turtle

class Paddles(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.resizemode('user')
        self.penup()
        self.speed(0)
        self.goto(position)


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

