from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(xpos, ypos)

    def go_up(self):
        if self.ycor() < 270:
            self.sety(self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -270:
            self.sety(self.ycor() - 20)
