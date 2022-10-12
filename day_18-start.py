from turtle import Turtle, Screen

timmy = Turtle()
timmy.color('MediumVioletRed')


timmy.speed(5)
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


# colors = ['red', 'green', 'purple', 'yellow', 'black', 'SlateBlue', 'MediumVioletRed', 'orange', 'salmon']
# timmy.pendown()

# Random walk
# def draw(num_sides):
#     timmy.color(random.choice(colors))
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)

# for sides in range(3, 11):
#     draw(sides)


timmy.pendown()
timmy.hideturtle()
timmy.pensize(10)
random_heading = [0, 90, 180, 270]
colors = ['SlateBlue', 'MediumVioletRed', 'DeepPink', 'OrangeRed', 'Gold', 'Tan', 'Khaki', 'Chartreuse', 'Cyan', 'DodgerBlue', 'Blue', 'DimGray', 'Gainsboro']

def draw(side):
    for _ in range(side):
        timmy.color(random.choice(colors))
        timmy.forward(25)
        timmy.setheading(random.choice(random_heading))
        

    
for side in range(100):
    draw(side)



screen = Screen()
screen.screensize(canvwidth=300, canvheight=300)
screen.exitonclick()