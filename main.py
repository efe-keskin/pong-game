from turtle import Screen
from scoreboard_1 import Score
from scoreboard_2 import Score2
from paddles import Paddle
from ball import Ball
from middleliner import MiddleLiner
import time

screen = Screen()
screen.tracer(0)
screen.listen()
top = Ball()
score = Score()
score2 = Score2()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
ortaline = MiddleLiner()
game_is_on = True

paddle_r = Paddle(370, 0)
paddle_l = Paddle(-370, 0)

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

while game_is_on:
    time.sleep(top.move_speed)
    screen.update()
    top.move()
    if top.ycor()>280 or top.ycor()<-280:
        top.bounce()

    if top.xcor() == 380:
        score.add_score()
        top.home()
        top.move_speed = 0.1
        top.bounce2()

    if top.xcor() == -380:
        score2.add_score()
        top.home()
        top.move_speed = 0.1
        top.bounce2()

    if (top.xcor()>340 or top.xcor()<-340) and(top.distance(paddle_r)<50 or top.distance(paddle_l)<50):
        top.bounce2()
        top.move_speed *=0.9





screen.exitonclick()
