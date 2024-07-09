from turtle import Turtle
import random

# Create a Food class to represent the food in the Snake game
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  # Set the food's shape to a circle
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Adjust the size of the food
        self.color("purple")  # Set the color of the food to purple
        self.speed("fastest")  # Set the drawing speed to the fastest possible
        self.refresh()  # Initialize the food's position

    def refresh(self):
        # Generate random coordinates for the food within the game boundaries
        random_x = random.randrange(-280, 280, 20)  # X-coordinate in increments of 20
        random_y = random.randrange(-280, 280, 20)  # Y-coordinate in increments of 20
        self.goto(random_x, random_y)  # Move the food to the new random position
