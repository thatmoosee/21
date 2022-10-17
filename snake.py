from turtle import Turtle as t
from turtle import Screen as s
import time
screen = s()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    segments = []
    START_POS = [(0, 0), (-20, 0), (-40, 0)]
    def __init__(self):
        screen = s()
        screen.setup(width=600, height=600)
        screen.bgcolor('black')
        screen.title('Snake')



    def create_snake(self):
        for position in self.START_POS:
            new_segment = t("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)
        self.head = self.segments[0]

    def move(self):
        game_is_on = True

        screen.update()
        time.sleep(0.2)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def add_snake(self):
        new_segment = t("square")
        new_segment.penup()
        new_segment.color("white")
        self.segments.append(new_segment)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)