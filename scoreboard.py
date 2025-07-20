# Importing Turtle class from turtle module
from turtle import Turtle

# Constants for text alignment and font style
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Scoreboard class to display and update the score
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()      # Inheriting from the Turtle class
        self.score = 0
        self.penup()
        self.color("White")
        self.goto(0, 265)
        self.update_scoreboard()
        self.hideturtle()

    # Function to display the current score
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Function to show "GAME OVER" message
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # Function to increase the score and update the display
    def increase_score(self):
        self.score += 1
        self.clear()       # Clear the previous score text
        self.update_scoreboard()
