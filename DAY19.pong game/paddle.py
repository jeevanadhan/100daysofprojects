from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")  # Set paddle color
        self.shape("square")  # Set paddle shape
        self.penup()  # Prevent drawing lines while moving
        self.shapesize(stretch_len=1, stretch_wid=5)  # Resize paddle dimensions
        self.goto(position)  # Position the paddle

    def go_up(self):
        if self.ycor() < 250:  # Limit upward movement
            ycor = self.ycor() + 30  # Move paddle up
            self.goto(self.xcor(), ycor)

    def go_down(self):
        if self.ycor() > -250:  # Limit downward movement
            ycor = self.ycor() - 30  # Move paddle down
            self.goto(self.xcor(), ycor)
