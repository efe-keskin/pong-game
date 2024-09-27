from turtle import Turtle


class Score2(Turtle):
    def __init__(self):
        super().__init__()
        self.score2 = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(40, 260)
        self.write(f"{self.score2}", False, "center", ("Arial", 25, "normal"))

    def add_score(self):
        self.score2 += 1
        self.clear()
        self.write(f"{self.score2}", False, "center", ("Arial", 25, "normal"))
