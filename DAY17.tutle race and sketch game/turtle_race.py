import turtle,random
from turtle import Screen, Turtle
screen=Screen()
colors=["red","blue","black","green","violet"]
user_bet=screen.textinput(title="make your bet",prompt="which turtle  will win enter a color:")
screen.setup(width=500,height=400)
yaxis=-100
all_turtle_address=[]
for i in range(5):
    dummy = Turtle(shape="turtle")
    dummy.penup()
    dummy.goto(x=-230,y=yaxis)
    dummy.color(colors[i])
    yaxis+=50
    all_turtle_address.append(dummy)
is_race_on=False
if user_bet:
    is_race_on=True
while is_race_on:
    ran_move=random.randint(1,5)
    ran_turtle=random.randint(0,4)
    if all_turtle_address[ran_turtle].xcor()>220:
        is_race_on=False
        winner=all_turtle_address[ran_turtle].pencolor()
        if user_bet==winner:
            print(f"you won the game {winner} turtle is first")
        else:
            print(f"you lose the game the {winner} turtle is first ")
    all_turtle_address[ran_turtle].forward(ran_move)

screen.exitonclick()
