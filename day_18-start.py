from turtle import Turtle, Screen

timmy = Turtle()
timmy.color('MediumVioletRed')


timmy.speed(1)
# for _ in range(4):
#     timmy.dot(20, 'SlateBlue')
#     timmy.forward(200)
#     timmy.left(90)


# timmy.penup()
# timmy.setposition(-400, 0)
# timmy.pencolor('black')
# for _ in range(20):
#     timmy.pendown()
#     timmy.forward(20)
#     timmy.penup()
#     timmy.forward(20)

# timmy.hideturtle()


import random


colors = ['red', 'green', 'purple', 'yellow', 'black', 'SlateBlue', 'MediumVioletRed', 'orange', 'salmon']
timmy.pendown()
accu = 3

while accu != 10:
    timmy.color(random.choice(colors))
    for _ in range(accu):
        if accu == 7:
            divide_by = 51
        else:
            divide_by = int(360 / accu)
            timmy.forward(120)
            timmy.right(divide_by)

    accu += 1



screen = Screen()
screen.exitonclick()