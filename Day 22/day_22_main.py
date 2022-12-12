import time
from turtle import Screen
from day_22_player import Player
from day_22_car_manager import CarManager
from day_22_scoreboard import Scoreboard


screen = Screen()
screen.setup()
screen.tracer(0)

player = Player()
car_manager = CarManager()
# Create a score board with current level of cars and if game over
scoreboard = Scoreboard()

game_is_on = True   
while game_is_on:
    # Create a turtle object
    car_manager.create_cars()
    time.sleep(0.1)
    screen.update()
    # Create multiple cars and move them to the left
    car_manager.move_the_car()

    # If car crashes the turtle then break
    for item in car_manager.all_cars:
        if item.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Move it forward
    screen.listen()
    screen.onkeypress(player.move_up, 'Up')

    # If turtle gets to the top then restart position and increase speed of cars
    if player.ycor() > player.FINISH_LINE_Y:
        player.finish_line()
        scoreboard.level_up()
        car_manager.increase_speed()

    

screen.exitonclick()

