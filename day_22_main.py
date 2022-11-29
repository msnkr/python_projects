import time
from turtle import Screen
from day_22_player import Player
from day_22_car_manager import CarManager
from day_22_scoreboard import Scoreboard


screen = Screen()
screen.setup()
screen.tracer(0)

timmy = Player()
car = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    score.current_level()
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    screen.listen()
    screen.onkeypress(timmy.move_up, 'Up')

    for x in car.cars_list:
        if timmy.distance(x) < 15:
            score.game_over()
            game_is_on = False
    
    if timmy.turtle_still_going():
        timmy.go_to_start()
        car.level_up()


screen.exitonclick()