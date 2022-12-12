from turtle import Turtle, Screen
import time
from day_21_paddles import Paddles
from day_21_ball import Ball
from day_21_scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.tracer(0)

# Draw lines top and bottom
line = Turtle()
line.goto(-380, 300)
line.color('white')
line.hideturtle()
line.forward(750)

line2 = Turtle()
line2.goto(-380, -300)
line2.color('white')
line2.hideturtle()
line2.forward(750)
######

# Create paddle and ball objects
right_paddle = Paddles((400, 0))
left_paddle = Paddles((-400, 0))
ball = Ball()
score = Scoreboard()

# Listen for events from keyboard and call func
screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')

game_is_on = True
while game_is_on:
    ball.move_ball()
    time.sleep(ball.move_speed)
    screen.update()

    # Bounce off y coordinates
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Bounce in x position if hits the paddle and wall if they're in distance with eachother
    if ball.distance(right_paddle) < 50 and ball.xcor() > 380 or ball.distance(left_paddle) < 50 and ball.xcor() < -380:
        ball.bounce_x()

    # Detect if ball goes past the xcoordinates without the left paddle
    if ball.xcor() > 400:
        ball.reset()
        score.left_point()

    # Detect if ball goes past xcoordinate without right paddle
    if ball.xcor() < -400:
        ball.reset()
        score.right_point()

screen.exitonclick()