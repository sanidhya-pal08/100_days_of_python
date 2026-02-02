import turtle
from turtle import Turtle,Screen
import random
from random import randrange
direction=[90,180,270,0]
timmy=Turtle()
timmy.speed("fastest")
timmy.shape("turtle")
screen=Screen()
timmy.pensize(15)
screen.colormode(255)
for i in range(0,100):
    R = randrange(0,257,10)
    G = randrange(0,257,10)
    B = randrange(0,257,10)
    timmy.color(R,G,B)
    timmy.left(random.choice(direction))
    timmy.forward(20)



screen.exitonclick()