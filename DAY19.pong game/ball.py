from turtle import Turtle

# Define the Ball class, which inherits from the Turtle class
class Ball(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.penup()  # Lift the pen to avoid drawing while moving
        self.shape("circle")  # Set the ball's shape to a circle
        self.color("white")  # Set the ball's color to white
        self.x = 10  # Initial horizontal movement increment
        self.y = 10  # Initial vertical movement increment
        self.move_speed = 0.1  # Initial speed of the ball (used for time delay in the game loop)

    # Method to move the ball on the screen
    def move(self):
        new_xcor = self.xcor() + self.x  # Calculate the new x-coordinate
        new_ycor = self.ycor() + self.y  # Calculate the new y-coordinate
        self.goto(new_xcor, new_ycor)  # Move the ball to the new position

    # Method to reverse the ball's vertical direction (y-axis)
    def bounce_y(self):
        self.y = self.y * -1  # Reverse the direction of movement along the y-axis

    # Method to reverse the ball's horizontal direction (x-axis)
    def bounce_x(self):
        self.x = self.x * -1  # Reverse the direction of movement along the x-axis
        self.move_speed *= 0.9  # Increase the speed of the ball by reducing the delay

    # Method to reset the ball to the center of the screen
    def reset(self):
        self.goto(0, 0)  # Move the ball back to the center
        self.x = self.x * -1  # Reverse the horizontal direction for the next serve
        self.move_speed = 0.1  # Reset the speed to the initial value
