import turtle
from turtle import Turtle,Screen
tom=Turtle()
screen=Screen()

def move_forward():
    tom.forward(10)
def move_backwards():
    tom.backward(10)
def anti_clockwise():
    tom.left(10)
def clockwise():
    tom.right(10)
def clearscreen():
    tom.reset()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=anti_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clearscreen)
screen.exitonclick()
