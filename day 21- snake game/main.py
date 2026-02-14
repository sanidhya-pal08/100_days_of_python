from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# controls
screen.listen()
screen.onkey(snake.go_up, "w")
screen.onkey(snake.go_down, "s")
screen.onkey(snake.go_left, "a")
screen.onkey(snake.go_right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # food collision
    if snake.head.distance(food) < 15:
        food.move_food()
        snake.increase_size()
        scoreboard.increase_score()

    # wall collision
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        scoreboard.reset()
        snake.reset()

    # tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
