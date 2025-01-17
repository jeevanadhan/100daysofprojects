FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level_up()
    def level_up(self):
        self.clear()
        self.goto(-230, 260)
        self.write("level: ", align="center", font=("Courier", 24, "normal"))
        self.goto(-180, 260)
        self.write(self.level, align="center", font=("Courier", 24, "normal"))
        self.level+=1
    def game_over(self):
        self.goto(0,0)
        self.color("black")
        self.write("game over", align="center", font=("Courier",24,"normal"))

