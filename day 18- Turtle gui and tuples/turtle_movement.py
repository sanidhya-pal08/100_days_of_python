from turtle import Turtle,Screen
jimmy=Turtle()
jimmy.shape("turtle")

# for i in range (0,10):
#     jimmy.color("black")
#     jimmy.forward(10)
#     jimmy.color("white")
#     jimmy.forward(10)
# jimmy.color("black")

for i in range(0,10):
    jimmy.pendown()
    jimmy.forward(10)
    jimmy.penup()
    jimmy.forward(10)
    
jimmy.pendown()
screen=Screen()
screen.exitonclick()
