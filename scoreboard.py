from turtle import Turtle

# Constants for text alignment and font settings
ALIGNMENT = 'center'
FONT = ('Stencil', 20, 'normal')

# Create a Scoreboard class to keep track of and display the player's score
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Initialize the score to 0
        self.hideturtle()
        self.goto(x=0, y=270)  # Position the scoreboard at the top center of the screen
        self.color("white")
        self.update_scoreboard()

    # Update the scoreboard with the current score
    def update_scoreboard(self):
        self.clear()  # Clear the previous score
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Display "Game Over" message when the game ends
    def game_over(self):
        self.goto(x=0, y=0)  # Position the "Game Over" message at the center of the screen
        self.write(arg="Game Over.", align=ALIGNMENT, font=FONT)

    # Increase the player's score by 1 and update the scoreboard
    def increase_score(self):
        self.score += 1
        self.clear()  # Clear the previous score
        self.update_scoreboard()
