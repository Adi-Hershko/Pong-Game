from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(starting_position)

    def go_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)
