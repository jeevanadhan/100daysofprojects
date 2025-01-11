from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.pensize(width=20)
        self.color("White")
        self.goto(0,260)
        self.write(f"score = {self.score} ", move=False, align="center", font=("Courier", 15, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Courier",15,"normal"))


    def score_inc(self):
        self.clear()
        self.write(f"score = {self.score} ", move=False, align="center", font=("Courier", 15, "normal"))

