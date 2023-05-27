from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

# Creating the screen with name and size
screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Command keys
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400 or ball.xcor() < - 400:
        screen.exitonclick()
