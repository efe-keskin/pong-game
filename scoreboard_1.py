from turtle import Turtle, Screen


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-40, 260)
        self.write(f"{self.score}", False, "center", ("Arial", 25, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, "center", ("Arial", 25, "normal"))
