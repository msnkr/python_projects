from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10




class CarManager():

    def __init__(self):
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 5
        

    def create_cars(self):
        random_choice = random.randint(1, 6)
        if random_choice == 6:
            self.car = Turtle('square')
            self.car.shapesize(stretch_len=2, stretch_wid=1)
            self.car.penup()
            self.car.goto(350, random.randint(-230, 230))
            self.car.color(random.choice(COLORS))
            self.all_cars.append(self.car)


    def move_the_car(self):
        for car in self.all_cars:
            car.backward(self.STARTING_MOVE_DISTANCE)


    def increase_speed(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT
