from turtle import Turtle, Screen


screen = Screen()
screen.title('My snake game')
screen.bgcolor('black')
x_position = [-0, -20, -40]

for x in x_position:
    snake = Turtle(shape='square')
    snake.color('white')
    snake.goto(x, 0)



screen.exitonclick()