from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RANDOM_X = []


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_len=4, stretch_wid=2)
        self.change_color()
        self.random_location()


    def car_move(self):
        self.forward(STARTING_MOVE_DISTANCE)
    

    def change_color(self):
        self.color(random.choice(COLORS))

    
    def random_location(self):
        self.goto(300, random.randint(-230, 230))