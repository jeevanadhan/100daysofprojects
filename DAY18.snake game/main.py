
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score_board import Scoreboard
score=Scoreboard()
food=Food()
snake = Snake()
screen=Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)
    if snake.snake_head.distance(food) < 20:
        food.refresh()
        score.score+=1
        snake.extend()
        score.score_inc()
    if snake.snake_head.xcor()>280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor()>280 or snake.snake_head.ycor()<-280:
        game_is_on=False
        score.game_over()
    for segments in snake.segment[1:]:
        if snake.snake_head.distance(segments) < 10:
            game_is_on=False
            score.game_over()
screen.exitonclick()