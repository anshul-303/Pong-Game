from turtle import Turtle
class Paddle(Turtle):
    def  __init__(self, positionx, positiony):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5, 5, 0.5)
        self.color("white")
        self.penup()
        self.speed(3)
        self.setheading(90)
        self.goto(positionx, positiony)

    def up_w(self):
        self.forward(40)

    def down_s(self):
        self.backward(40)

    def up_up(self):
        self.forward(40)

    def down_down(self):
        self.backward(40)




