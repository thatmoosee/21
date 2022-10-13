from turtle import Screen as s
from turtle import Turtle as t
screen = s()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('Snake')

one = t()
two = t()
three = t()
blocks = [one,two,three]
start_pos=[(0,0),(-20,0),(-40,0)]
pos = 0
for i in blocks:
    i.penup()
    i.shape('square')
    i.color('white')
    i.back(pos)
    pos = pos + 20




screen.exitonclick()