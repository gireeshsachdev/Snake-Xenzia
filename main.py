from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Create a Turtle screen object and set its dimensions, background color, and title
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0)

# Create Snake, Food, and Scoreboard instances
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for key presses and associate them with Snake's movement methods
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

# Initialize the game loop
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with Wall
    if abs(snake.head.xcor()) > 282 or abs(snake.head.ycor()) > 282:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with Tail
    for body_piece in snake.snake_body[1:]:
        if snake.head.distance(body_piece) < 10:
            game_is_on = False
            scoreboard.game_over()

# Allow the user to exit the game by clicking on the screen
screen.exitonclick()
