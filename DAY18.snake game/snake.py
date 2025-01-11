import turtle
from turtle import Screen,Turtle

segment_position = [(0, 0), (-20, 0), (-40, 0)]
down=270
up=90
right=0
left=180

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.snake_head= self.segment[0]
    def create_snake(self):
        for position in segment_position:
            self.add_segment(position)
    def add_segment(self,position):
        new_seg = Turtle()
        new_seg.color("white")
        new_seg.shape("square")
        new_seg.penup()
        new_seg.goto(position)
        self.segment.append(new_seg)
    def extend(self):
        self.add_segment(self.segment[-1].position())
    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            xax = self.segment[seg - 1].xcor()
            yax = self.segment[seg - 1].ycor()
            self.segment[seg].goto(xax, yax)
        self.segment[0].forward(20)
    def up(self):
        if self.segment[0].heading() != down:
            self.segment[0].setheading(90)
    def down(self):
        if self.segment[0].heading() != up:
            self.segment[0].setheading(270)
    def left(self):
        if self.segment[0].heading() != right:
            self.segment[0].setheading(180)
    def right(self):
        if self.segment[0].heading() != left:
            self.segment[0].setheading(0)
