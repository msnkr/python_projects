from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend_segments(self):  
        # Extend snake
        self.add_segments(self.segments[-1].position())


    def create_snake(self):
        # Create snake
        for i in COORDINATES:
            self.add_segments(i)


    def add_segments(self, position):
            # Create a square turtle object
            snake = Turtle(shape='square')
            snake.penup()
            snake.color('white')
            snake.goto(position)
            self.segments.append(snake) # This saves the actual turtle objects. You don't only have to append i.


    def move(self):
        # Move snake
        for seg in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg -1].xcor()
            new_y = self.segments[seg -1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)