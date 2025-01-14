from turtle import Turtle, Screen
from paddle import Paddle
from pong_ball import Ball
import time
import random




screen=Screen()
screen.setup(800, 600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

r_paddle=Paddle(390,0)
l_paddle=Paddle(-395,0)
ball=Ball()
line_turt=Turtle()
line_turt.color("white")
line_turt.penup()
line_turt.goto(0, 400)
line_turt.setheading(270)
line_turt.pendown()
p=0

while p<35:
    line_turt.forward(10)
    line_turt.penup()
    line_turt.forward(10)
    line_turt.pendown()
    p+=1

l_scoreboard = Turtle()
l_scoreboard.hideturtle()
l_scoreboard.penup()
l_scoreboard.color("white")
l_scoreboard.goto(-200, 250)
l_score=0
l_scoreboard.write(f"Score : {l_score}", align="center", font=("Arial", 24, "bold"))

r_scoreboard = Turtle()
r_scoreboard.hideturtle()
r_scoreboard.penup()
r_scoreboard.color("white")
r_scoreboard.goto(200, 250)
r_score=0
r_scoreboard.write(f"Score : {l_score}", align="center", font=("Arial", 24, "bold"))


screen.onkey(fun=l_paddle.up_w, key="w")
screen.onkey(fun=l_paddle.down_s, key="s")
screen.onkey(fun=r_paddle.up_up, key="Up")
screen.onkey(fun=r_paddle.down_down, key="Down")

game_is_on=True
gameover=Turtle()
gameover.hideturtle()  # Hide the turtle cursor
gameover.penup()       # Lift the pen to avoid drawing
gameover.color("white")  # Set text color
gameover.goto(0, 0)

while game_is_on :
    time.sleep(0.03)
    screen.update()
    ball.move_r()
    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.bounce_wall()

    if ball.distance(r_paddle)<=65 and ball.xcor()>370 :
        ball.bounce_paddle()

    if ball.distance(l_paddle)<=65 and ball.xcor()<-370 :
        ball.bounce_paddle()

    if ball.distance(r_paddle)>65 and ball.xcor()>410 :
        l_score += 1
        l_scoreboard.clear()
        l_scoreboard.write(f"Score : {l_score}", align="center", font=("Arial", 24, "bold"))
        time.sleep(1)
        ball.goto(0,0)
        ball.reset_position()


    if ball.distance(l_paddle)>65 and ball.xcor()<-410 :
        r_score += 1
        r_scoreboard.clear()
        r_scoreboard.write(f"Score : {r_score}", align="center", font=("Arial", 24, "bold"))
        time.sleep(1)
        ball.reset_position()

    if l_score==10 or r_score==10:
        gameover.write("Game Over.", align="center", font=("Arial", 24, "bold"))
        game_is_on=False

screen.exitonclick()


