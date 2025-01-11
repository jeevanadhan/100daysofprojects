import turtle
import colorgram
import random
from turtle import Screen ,Turtle,colormode
colormode(255)
dummy=Turtle()
screen=Screen()
colors=colorgram.extract("images.jpg",20)
color_list=[]
for i in colors:

    r=i.rgb.r
    g=i.rgb.g
    b=i.rgb.b
    color_tuple=(r,g,b)
    color_list.append(color_tuple)
dummy.penup()
dummy.hideturtle()
def oneline():
    for i in range(10):
        if i<=9:
            dummy.dot(25,random.choice(color_list))
            dummy.forward(60)
        else:
            dummy.dot(25,random.choice(color_list))

n=-240
for i in range(10):
    dummy.teleport(-280,n)
    oneline()
    n+=53
screen.exitonclick()
