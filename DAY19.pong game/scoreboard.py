from turtle import Turtle

# Define the Scoreboard class, which inherits from the Turtle class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.color("white")  # Set the text color to white
        self.penup()  # Lift the pen to avoid drawing lines
        self.hideturtle()  # Hide the turtle shape, as only text is displayed
        self.l_scor = 0  # Initialize the left player's score
        self.r_scor = 0  # Initialize the right player's score
        self.update_scoreboard()  # Display the initial scoreboard

    # Method to update and display the scoreboard
    def update_scoreboard(self):
        self.clear()  # Clear the previous scoreboard to avoid overlapping text
        # Display the left player's score
        self.goto(-100, 200)  # Move to the left score position
        self.write(self.l_scor, align="center", font=("Courier", 50, "normal"))
        # Display the right player's score
        self.goto(100, 200)  # Move to the right score position
        self.write(self.r_scor, align="center", font=("Courier", 50, "normal"))

    # Method to increment and update the left player's score
    def l_score(self):
        self.l_scor += 1  # Increment the left player's score by 1
        self.update_scoreboard()  # Update the scoreboard to reflect the new score

    # Method to increment and update the right player's score
    def r_score(self):
        self.r_scor += 1  # Increment the right player's score by 1
        self.update_scoreboard()  # Update the scoreboard to reflect the new score
