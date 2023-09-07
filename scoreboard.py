from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setpos(0, 270)
        self.penup()
        self.ht()
        self.color("white")
        self.speed("fastest")
        self.increase_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score : {self.score}", move=False, align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.setpos(0, 0)
        self.write(arg="Game Over", move=False, align="center", font=("Courier", 40, "normal"))


    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
