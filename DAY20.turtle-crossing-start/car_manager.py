from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars=[]
        self.colors=["red", "orange", "yellow", "green", "blue", "purple"]
        self.speed=40

    def create_cars(self,position):
        dummy=Turtle()
        dummy.penup()
        dummy.shape("square")
        dummy.shapesize(stretch_wid=1,stretch_len=2)
        dummy.color(random.choice(self.colors))
        dummy.goto(position)
        self.cars.append(dummy)

    def move(self):
        for car in self.cars:
            car_x=car.xcor()-self.speed
            car_y=car.ycor()
            car.goto(car_x,car_y)

