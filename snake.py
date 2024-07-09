from turtle import Turtle

# Constants for initial snake positions and movement distance
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# Constants for directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Create a Snake class to represent the snake in the game
class Snake:
    def __init__(self):
        # Initialize the snake's body as an empty list
        self.snake_body = []
        # Create the initial snake
        self.create_snake()
        # Set the snake's head as the first body piece
        self.head = self.snake_body[0]

    def create_snake(self):
        # Create the initial snake with three body pieces
        for position in STARTING_POSITIONS:
            self.add_body(position)

    def add_body(self, position):
        # Create a new body piece for the snake
        body_piece = Turtle(shape="square")
        body_piece.color("white")
        body_piece.penup()
        body_piece.goto(position)
        # Add the body piece to the 'snake_body' list
        self.snake_body.append(body_piece)

    def extend(self):
        # Add a new body piece to the snake
        self.add_body(self.snake_body[-1].position())

    def move(self):
        # Move the snake by updating the positions of its body pieces
        for piece_num in range(len(self.snake_body) - 1, 0, -1):
            new_position = self.snake_body[piece_num - 1].position()
            self.snake_body[piece_num].goto(new_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Allow the snake to turn up only if it's not moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Allow the snake to turn down only if it's not moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Allow the snake to turn left only if it's not moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Allow the snake to turn right only if it's not moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
