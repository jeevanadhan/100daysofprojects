from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Initialize the scoreboard to keep track of scores
score = Scoreboard()

# Set up the screen
screen = Screen()
screen.bgcolor("#000000")  # Set the background color to black
screen.tracer(0)  # Turn off automatic screen updates for smoother animations
screen.setup(width=800, height=600)  # Set the screen dimensions

# Create the left and right paddles at their respective starting positions
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

# Create the ball object
ball = Ball()

# Listen for keyboard inputs to move the paddles
screen.listen()
screen.onkey(right_paddle.go_up, "Up")  # Move right paddle up when "Up" key is pressed
screen.onkey(right_paddle.go_down, "Down")  # Move right paddle down when "Down" key is pressed
screen.onkey(left_paddle.go_up, "w")  # Move left paddle up when "w" key is pressed
screen.onkey(left_paddle.go_down, "s")  # Move left paddle down when "s" key is pressed

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Control the ball's speed by adding a delay
    screen.update()  # Refresh the screen after each frame
    ball.move()  # Move the ball in the current direction

    # Check for collision with the top or bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # Reverse the ball's vertical direction if it hits the wall

    # Check for collision with the paddles
    if (320 < ball.xcor() < 340 and right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50) or \
            (-340 < ball.xcor() < -320 and left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50):
        ball.bounce_x()  # Reverse the ball's horizontal direction if it hits a paddle

    # Check if the ball goes past the right edge
    if ball.xcor() > 380:
        ball.reset()  # Reset the ball to the center of the screen
        score.l_score()  # Increment the left player's score

    # Check if the ball goes past the left edge
    if ball.xcor() < -380:
        ball.reset()  # Reset the ball to the center of the screen
        score.r_score()  # Increment the right player's score

# Exit the game when the screen is clicked
screen.exitonclick()
