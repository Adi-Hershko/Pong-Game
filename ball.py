from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def reset_speed(self):
        self.x_move = 10
        self.y_move = 10

    def increase_speed(self):
        self.x_move += 2.5
        self.y_move += 2.5

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.bounce_x()
        time.sleep(1)
        self.home()