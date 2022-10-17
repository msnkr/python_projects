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


# timmy.pendown()
# timmy.hideturtle()
# timmy.pensize(10)
# random_heading = [0, 90, 180, 270]
# colors = ['#083836', '#66D37E', '#C6E872', '#FBFFA3', '#E1FFB1', '#C7F2A4', '#B6E388', '#B6E388']

# for _ in range(500):
#     timmy.color(random.choice(colors))
#     timmy.forward(30)
#     timmy.setheading(random.choice(random_heading))
    


# screen = Screen()
# screen.exitonclick()



class RandomWalk:
    
    def __init__(self):
        self.timmy = Turtle()
        self.colors = ['#083836', '#66D37E', '#C6E872', '#FBFFA3', '#E1FFB1', '#C7F2A4', '#B6E388', '#B6E388']
        self.timmy.speed(0) 


    def random_walk(self, number):
        destination = [0, 90, 180, 270]
        for _ in range(number):
            self.timmy.hideturtle()
            self.timmy.pensize(15)
            self.timmy.pencolor(random.choice(self.colors))
            self.timmy.forward(30)
            self.timmy.setheading(random.choice(destination))


    def call_diagrams(self):
        for sides in range(3, 11):
            self.draw_diagrams(sides)

    
    def draw_diagrams(self, sides):
        self.timmy.color(random.choice(self.colors))
        angle = 360 / sides
        for _ in range(sides):
            self.timmy.forward(100)
            self.timmy.right(angle)

   
        
RandomWalk().call_diagrams()
# RandomWalk().random_walk(100)
screen = Screen()
screen.exitonclick()


