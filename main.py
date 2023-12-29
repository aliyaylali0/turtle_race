import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
all_turtles = []
def create_turtle():
    colors = ["red", "green", "yellow", "blue", "pink", "orange"]
    x = -230
    y = -170

    for new_turtle in range(6):
        y += 50

        new_turtle = Turtle(shape="turtle")
        selected_color = random.choice(colors)
        new_turtle.color(selected_color)
        colors.remove(selected_color)
        new_turtle.penup()
        new_turtle.goto(x, y)
        all_turtles.append(new_turtle)


screen = Screen()

screen.setup(width=500,height=400)

user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
create_turtle()

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winnig_color = turtle.pencolor()
            if winnig_color == user_bet:
                print(f"You have won! {winnig_color} turtle is the winner!")
            else:
                print(f"You lose! {winnig_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()