from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

# Creating the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)    # Turning off screen auto-refresh for smooth animation

# Creating snake, food, and scoreboard objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listening for keyboard input to control the snake
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# Main game loop
is_game_on = True
while is_game_on:
    screen.update()     # Refresh the screen manually
    time.sleep(0.1)     # Pause for 0.1 seconds to control snake speed
    snake.move()        # Move the snake forward

#     detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#     detect collision with wall
    if (
            snake.head.xcor()> 280 or
            snake.head.xcor()< -280 or
            snake.head.ycor()> 280 or
            snake.head.ycor()< -280
    ):
        is_game_on = False
        scoreboard.game_over()

    #     detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

# Exit screen when clicked
screen.exitonclick()