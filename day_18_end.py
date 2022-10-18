# import colorgram
import random
from turtle import Turtle, Screen


# get_colors_list = []
# colors = colorgram.extract('hirst-painting.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors = (r, g, b)
#     get_colors_list.append(rgb_colors)

color_list = [(203, 165, 108), (239, 245, 240), (235, 238, 244), (154, 74, 47), (222, 201, 136), (51, 93, 124), (171, 153, 40), (138, 31, 20), (132, 162, 185), (199, 91, 71), (47, 122, 88), (14, 100, 73), (146, 178, 147), (94, 73, 75), (72, 48, 39), (234, 176, 164), (162, 143, 158), (55, 46, 50), (184, 205, 172), (19, 85, 88), (42, 62, 74), (147, 20, 23), (85, 145, 127), (183, 86, 88), (45, 66, 84), (107, 127, 152), (221, 172, 176), (14, 72, 67)]



def create_10():
    tim.setpos(-250, -new_pos)
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


tim = Turtle()
screen = Screen()

tim.penup()
new_pos = 250
tim.speed(7)
screen.colormode(255)
tim.hideturtle()


for _ in range(10):
    create_10()
    new_pos -= 50

    
screen.exitonclick()


