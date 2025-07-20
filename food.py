from random import randint  # Importing randint to generate random coordinates
from turtle import Turtle  # Importing Turtle class to use as food

# Food class to create and place food on the screen
class Food(Turtle):
    def __init__(self):
        super().__init__()  # Inheriting from the Turtle class
        self.shape("circle")  # Shape of the food is a circle
        self.penup()  # No drawing while moving
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Making the circle small (10x10)
        self.color("Blue")  # Food color is blue
        self.speed("fastest")  # Fastest animation for food appearance
        self.refresh()  # Place the food at a random location when created

    # Function to move food to a new random position
    def refresh(self):
        random_x = randint(-280, 280)  # Random X coordinate within screen bounds
        random_y = randint(-280, 280)  # Random Y coordinate within screen bounds
        self.goto(random_x, random_y)  # Move food to the new location
