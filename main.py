from turtle import Screen as s
from turtle import Turtle as t
from snake import Snake
from food import Food
import time
screen = s()
snake = Snake()
snake.create_snake()
screen.listen()
food = Food()

game_is_on = True
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
