from turtle import Turtle, Screen

dummy=Turtle()
dummy.shape("turtle")
screen=Screen()
def draw_shape(sides):
    angle=360/sides
    for j in range(sides):
        dummy.forward(100)
        dummy.right(angle)
for i in range(3,10):
    draw_shape(i)
    
screen.exitonclick()
