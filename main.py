from turtle import Turtle, Screen
import time
from ball import Ball
from createpaddle import CreatePaddle
from scoreboard import ScoreBoard

score = ScoreBoard()
screen = Screen()
ball = Ball()
TIME_VAL = 0.109

screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

l_paddle = CreatePaddle((350, 0))
r_paddle = CreatePaddle((-350, 0))

screen.onkey(l_paddle.move_up, "Up")
screen.onkey(l_paddle.move_down, "Down")

screen.onkey(r_paddle.move_up, "w")
screen.onkey(r_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(TIME_VAL)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect the collision
    if ball.distance(l_paddle) < 50 and l_paddle.xcor() > 320 or ball.distance(
            r_paddle) < 50 and r_paddle.xcor() < -320:
        ball.bounce_x()
        TIME_VAL -= 0.002

    # Detect when the co-ordinates miss the ball.
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.bounce_x()
        score.l_point()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.bounce_x()
        score.r_point()

screen.exitonclick()
