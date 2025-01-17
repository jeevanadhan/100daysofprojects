from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.move_distance=10
        self.color("red")
        self.finish_line=280
        self.yaxis=-280
        self.setheading(90)
        self.speed=0.5
        self.reset()
    def go_up(self):
        self.yaxis+=10
        self.goto(0,self.yaxis)
    def reset(self):
        self.yaxis=-280
        self.goto(0,self.yaxis)
        self.speed*=0.9


