from turtle import Turtle


class MiddleLiner(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.setposition(0, -270)
        self.hideturtle()
        self.color("white")
        for _ in range(11):
            self.pendown()
            self.forward(40)
            self.penup()
            self.forward(10)
