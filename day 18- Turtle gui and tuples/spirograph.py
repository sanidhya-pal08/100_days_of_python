import turtle
from turtle import Turtle
import random
timmy=Turtle()
r=50
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colorr=(r,g,b)
    return colorr
timmy.speed("fastest")
timmy.shape("turtle")

for i in range(0,72):
    timmy.color(random_color())
    timmy.circle(r)
    timmy.left(5)

screen=turtle.Screen()
screen.exitonclick()