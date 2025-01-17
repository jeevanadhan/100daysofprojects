import time
from scoreboard import Scoreboard
from turtle import Screen  # Correct import
from player import Player
from car_manager import CarManager
import random
screen = Screen()
screen.tracer(0)
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()
screen.setup(width=600, height=600)
screen.listen()
screen.onkey(player.go_up,"Up")
car_xax=280
game_is_on = True
while game_is_on:
    time.sleep(player.speed)
    screen.update()
    car_yax=random.randint(-240,280)
    position=(car_xax,car_yax)
    if random.randint(1,2)==1:
        car_manager.create_cars(position)
    if player.ycor()>280:
        player.reset()
        scoreboard.level_up()
    for cars in car_manager.cars:
        if player.distance(cars)<30:
            game_is_on=False
            scoreboard.game_over()
    car_manager.move()
screen.exitonclick()