from turtle import Turtle, Screen
import time



screen = Screen()
screen.title('My snake game')
screen.bgcolor('black')
x_position = [(-0, 0), (-20, 0), (-40, 0)]
segments = []
# screen.tracer(0)


for x in x_position:
    snake = Turtle(shape='square')
    snake.penup()
    snake.color('white')
    snake.goto(x)
    segments.append(snake)


go_forward = True
while go_forward:
    # screen.update()
    # time.sleep(0.1)

    for seg_num in range(len(segments) -1, 0, -1):
        x_coordinate = segments[seg_num -1].xcor()
        y_coordinate = segments[seg_num -1].ycor()
        segments[seg_num].goto(x_coordinate, y_coordinate)

    segments[0].left(90)

    

screen.exitonclick()