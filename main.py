from turtle import Screen as s
from turtle import Turtle as t
from snake import Snake

screen = s()
tim = Snake()
tim.create_snake()
tim.add_snake()
screen.listen()

game_is_on = True
while game_is_on:
    snake.move()
screen.exitonclick()