import time
from turtle import Screen
from day_22_player import Player
from day_22_car_manager import CarManager
# from day_22_scoreboard import Scoreboard


screen = Screen()
screen.setup()
screen.tracer(0)

player = Player()
car_manager = CarManager()

game_is_on = True   
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.listen()
    screen.onkeypress(player.move_up, 'Up')


screen.exitonclick()

# Create a turtle object
# Move it forward
# Create multiple cars and move them to the left
# If car crashes the turtle then break
# If turtle gets to the top then restart position and increase speed of cars
# Create a score board with current level of cars and if game over