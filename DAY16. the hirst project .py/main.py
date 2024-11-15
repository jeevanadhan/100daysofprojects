import turtle
import random
from turtle import Screen ,Turtle,colormode
colormode(255)
dummy=Turtle()
screen=Screen()
directions=[0,90,180,270]
dummy.speed("fastest")
def random_color():
    r=random.randint(0,250)
    g=random.randint(0,250)
    b=random.randint(0,250)
    tup=(r,g,b)

    return tup
angle=5
for i in range(72):
    dummy.color(random_color())
    dummy.circle(80)
    dummy.left(angle)
screen.exitonclick()