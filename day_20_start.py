from turtle import Turtle, Screen
import time


screen = Screen()
screen.title('My snake game')
screen.bgcolor('black')
screen.tracer(0)

coordinates = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for i in coordinates:
    snake = Turtle(shape='square')
    snake.penup()
    snake.color('white')
    snake.goto(i)
    segments.append(snake) # This saves the actual turtle objects. You don't only have to append i.

game_on = True
while game_on:
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)
        screen.update()


        if seg.xcor() > 400:
            game_on = False

screen.exitonclick()