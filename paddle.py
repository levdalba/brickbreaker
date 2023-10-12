from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def right(self):
        new_x = self.xcor() + 20
        if new_x < 350:
            self.goto(new_x, self.ycor())

    def left(self):
        new_x = self.xcor() - 20
        if new_x > -350:
            self.goto(new_x, self.ycor())
