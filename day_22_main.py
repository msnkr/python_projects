import time
from turtle import Screen
from day_22_player import Player
from day_22_car_manager import CarManager
# from day_22_scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Player()
car = CarManager()
car_positions = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    screen.listen()
    screen.onkeypress(timmy.move_up, 'Up')

    for x in car.cars_list:
        first_car = x[0]
        if first_car.xcor() == 0:
            break


screen.exitonclick()