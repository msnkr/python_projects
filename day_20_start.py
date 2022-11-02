from turtle import Turtle, Screen
import time
from day_20_snake import Snake


screen = Screen()
screen.title('My snake game')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
screen.listen()


screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()