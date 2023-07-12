from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Creating the screen
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=800, height=600)
screen.title("Pong")

# Creating paddles
left_paddle_pos = (-350, 0)
right_paddle_pos = (350, 0)

l_paddle = Paddle(left_paddle_pos)
r_paddle = Paddle(right_paddle_pos)

# Creating the ball
ball = Ball()

# Creating the scoreboard
scoreboard = Scoreboard()

# Moving the paddle
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()

    # Detect if the ball went over the right paddle
    if ball.xcor() > 380:
        ball.reset_speed()
        ball.reset()
        scoreboard.r_point()

    # Detect if the ball went over the right paddle
    if ball.xcor() < -380:
        ball.reset_speed()
        ball.reset()
        scoreboard.l_point()

screen.exitonclick()
