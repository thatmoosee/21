from turtle import Screen as s
from turtle import Turtle as t
from snake import Snake

screen = s()
snake = Snake()
snake.create_snake()
snake.add_snake()
screen.listen()

game_is_on = True
while game_is_on:
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.down, "Down")
    snake.move()

screen.exitonclick()