import turtle
import random
from turtle import Turtle
turtle.colormode(255)
timmy=Turtle()
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colorr=(r,g,b)
    return colorr
timmy.penup()
timmy.shape("circle")
def odd_even_check(a):
    if a%2==0:
        return True
    return False
number=0
for i in range(0,10):
    for i in range(0,10):
        timmy.forward(10)
        timmy.dot(4,random_color())
        
    if(odd_even_check(number)):
        timmy.right(90)
        timmy.forward(10)
        timmy.right(90)
        number+=1
    else:
        timmy.left(90)
        timmy.forward(10)
        timmy.left(90)
        number+=1
    

    
timmy
screen=turtle.Screen()
screen.exitonclick()