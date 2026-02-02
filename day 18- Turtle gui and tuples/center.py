from turtle import Turtle,Screen

from random import randint,randrange
timmy_the_turtle=Turtle()
timmy_the_turtle.shape("turtle")

screen=Screen()
screen.colormode(255)

for i in range(3,11):
    R = randrange(0,257,10)
    G = randrange(0,257,10)
    B = randrange(0,257,10)
    timmy_the_turtle.color(R,G,B)
    for j in range(0,i):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(360/i)


screen.exitonclick()