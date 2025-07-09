from turtle import  Screen
import time
from food import Food
from snake import  Snake
from  scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) <15:

        scoreboard.increase_score()
        food.move()
        snake.extend()
    #detect collision with wall

    if snake.head.xcor() >= 270 or snake.head.xcor() <= -270 or snake.head.ycor() >= 270 or snake.head.ycor() <= -270:
        game_is_on= False

    if snake.snake_touch():
        game_is_on = False


scoreboard.game_over()




screen.exitonclick()