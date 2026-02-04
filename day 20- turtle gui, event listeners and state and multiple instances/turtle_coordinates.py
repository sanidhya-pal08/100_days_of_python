from turtle import Turtle,Screen
import random
speed=[30,40,10,20]
tim=Turtle(shape="turtle")
jim=Turtle(shape="turtle")
gim=Turtle(shape="turtle")
him=Turtle(shape="turtle")
vim=Turtle(shape="turtle")

tim.penup()
jim.penup()
gim.penup()
him.penup()
vim.penup()
tim.color("blue")
jim.color("yellow")
gim.color("red")
him.color("purple")
vim.color("green")
all_turtles=[tim,jim,gim,him,vim]
screen=Screen()
screen.setup(height=500,width=700)
user_bet=screen.textinput(title="make your bet",prompt="which turtle will win the race and tell them to enter a color: ")

tim.goto(-330,200)
jim.goto(-330,150)
gim.goto(-330,100)
vim.goto(-330,50)
him.goto(-330,0)
is_race_on=True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>310:
            is_race_on=False
            winning_turtle=turtle
            if(user_bet==winning_turtle):
                print(f"you won {winning_turtle.pencolor()} won the race")
            else:
                print(f"you lost {winning_turtle.pencolor()} won the race")
        distances=random.choice(speed)
        turtle.forward(distances)
screen.exitonclick()