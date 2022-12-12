from turtle import Turtle, Screen
import random


# timmy = Turtle()
# timmy.color('MediumVioletRed')


# timmy.speed(0)
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


# timmy = Turtle()
# Screen().colormode(255)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tuple((r, g, b))


# timmy.pendown()
# timmy.hideturtle()
# timmy.pensize(10)
# random_heading = [0, 90, 180, 270]
# colors = random_colors()

# for _ in range(500):
#     timmy.color(random_colors())
#     timmy.forward(30)
#     timmy.setheading(random.choice(random_heading))
    

# screen = Screen()
# screen.exitonclick()



class RandomWalk:
    
    def __init__(self):
        self.timmy = Turtle()
        self.timmy.speed(0)
        self.screen = Screen()
        self.screen.colormode(255)


    def random_walk(self, number):
        destination = [0, 90, 180, 270]

        for _ in range(number):
            color = self.random_colors()
            self.timmy.hideturtle()
            self.timmy.pensize(15)
            self.timmy.pencolor(color)
            self.timmy.forward(30)
            self.timmy.setheading(random.choice(destination))


    def call_diagrams(self):
        for sides in range(3, 11):
            self.draw_diagrams(sides)

    
    def draw_diagrams(self, sides):
        self.timmy.color(self.random_colors())
        angle = 360 / sides
        for _ in range(sides):
            self.timmy.forward(100)
            self.timmy.right(angle)


    def famous_painting(self):
        self.timmy.hideturtle()
        self.timmy.penup()

        self.timmy.sety(-350)
        new_position = -350
        self.timmy.speed(0)
        self.timmy.setx(-400)
        for _ in range(15):
            for _ in range(11):
                self.timmy.dot(15, self.random_colors())
                self.timmy.forward(70)
                self.timmy.dot(15, self.random_colors())
                
            self.timmy.setx(-400)
            new_position += 50
            self.timmy.sety(new_position)


    def random_colors(self):
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        color = (self.r, self.g, self.b)
        return color


    def draw_spirograph(self, gap):
        for _ in range(int(360 / gap)):
            self.timmy.color(random_colors())
            th = self.timmy.heading()
            self.timmy.circle(100)
            self.timmy.setheading(th + gap)
    

# RandomWalk().call_diagrams()
# RandomWalk().random_walk(100)
# RandomWalk().famous_painting()
RandomWalk().draw_spirograph(5)


Turtle().speed(0)
Screen().exitonclick()