from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')


    def move_ball(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

        if self.ycor() > 200:
            new_y = self.ycor() - 20
            new_x = self.xcor() + 20

            self.goto(new_x, new_y)