from turtle import Turtle,Screen

def forward():
    tim.forward(40)
def backward():
    tim.backward(40)
def left():
    tim.left(30)
def right():
    tim.right(30)
tim=Turtle()
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen=Screen()
screen.listen()
screen.onkey(key="a",fun=left)
screen.onkey(key="s",fun=backward)
screen.onkey(key="w",fun=forward)
screen.onkey(key="c",fun=clear)
screen.onkey(key="d",fun=right)
screen.exitonclick()
