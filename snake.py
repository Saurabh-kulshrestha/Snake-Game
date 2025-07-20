from turtle import Turtle  # Importing the Turtle class

# Constants
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # Starting positions of snake segments
MOVE_DISTANCE = 20  # Distance the snake moves forward in each step
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

# Snake class to handle the snake's behavior
class Snake:
    def __init__(self):
        self.segments = []  # List to store snake segments
        self.create_snake()  # Create the initial snake body
        self.head = self.segments[0]  # First segment is considered the head

    # Create initial snake with 3 segments
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)  # Add each segment at the given position

    # Add a new segment to the snake
    def add_segment(self, position):
        new_segment = Turtle("square")  # Create a square turtle for each segment
        new_segment.color("white")  # Set the color of the segment to white
        new_segment.penup()  # Prevent drawing lines while moving
        new_segment.goto(position)  # Place the segment at the given position
        self.segments.append(new_segment)  # Add it to the segment list

    # Extend the snake (when it eats food)
    def extend(self):
        # Add a new segment at the position of the last segment
        self.add_segment(self.segments[-1].position())

    # Move the snake forward
    def move(self):
        # Move each segment to the position of the one in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    # Turn the snake up, if it's not currently going down
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Turn the snake down, if it's not currently going up
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Turn the snake right, if it's not currently going left
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # Turn the snake left, if it's not currently going right
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
