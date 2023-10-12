from turtle import Screen
from paddle import Paddle
from bricks import Bricks
import time


bricks = Bricks()
green_bricks = bricks(color="green", shot=2)
screen = Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.title("brick breaker")
screen.listen()
screen.tracer(0)
paddle = Paddle((0, -250))
screen.onkey(paddle.right, "Right")
screen.onkey(paddle.left, "Left")
while True:
    time.sleep(0)
    screen.update()


screen.exitonclick()
