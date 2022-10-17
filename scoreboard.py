from turtle import Turtle

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0,270)
        self.write(f"Score : {self.score}", align= "center", font=("Arial", 24, "normal"))
    def increase_Score(self):
        self.score+= 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))
    def game_over(self):
        print(f"Score: {self.score}")
        self.write("GAME OVER", align = "center", font=("Arial", 24, "normal"))