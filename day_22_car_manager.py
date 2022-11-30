from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager():

    def __init__(self):
        self.all_cars = []


    def create_cars(self):
        car_choice = random.randint(1, 6)
        if car_choice == 6:
            self.car = Turtle()
            self.car.shape('square')
            self.car.shapesize(stretch_len=2, stretch_wid=1)
            self.car.penup()
            self.car.color(random.choice(COLORS))
            self.car.goto(430, random.randint(-250, 250))
            self.all_cars.append(self.car)


    def move_car(self):
        self.car.backward(STARTING_MOVE_DISTANCE)
    