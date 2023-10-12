from turtle import Screen
from paddle import Paddle

# from bricks import Bricks
from ball import Ball
import time


# bricks = Bricks()
ball = Ball()
# green_bricks = bricks(color="green", shot=2)
screen = Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.title("brick breaker")
screen.listen()
screen.tracer(0)
paddle = Paddle((0, -250))
screen.onkey(paddle.right, "Right")
screen.onkey(paddle.left, "Left")
game_is_on = True
while game_is_on:
    time.sleep(0)
    screen.update()
    ball.start()


screen.exitonclick()
