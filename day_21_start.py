from turtle import Turtle, Screen
import time
from day_21_paddles import Paddles
from day_21_ball import Ball

screen = Screen()
screen.bgcolor('black')
screen.tracer(0)

right_paddle = Paddles((400, 0))
left_paddle = Paddles((-400, 0))
ball = Ball()


screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')

game_is_on = True
while game_is_on:
    ball.move_ball()
    time.sleep(0.1)
    screen.update()


screen.exitonclick()