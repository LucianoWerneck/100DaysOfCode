from turtle import Turtle, Screen
import random

is_race_on = False
new_turtle = Turtle()
scr = Screen()

scr.setup(width=500, height=400)
user_bet = scr.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
colors = ["red", "blue", "yellow", "orange", "green", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []
new_turtle. speed(3)

#Creating a Turtles, Positions and Colors
for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.reset()
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    new_turtle.color(colors[index])
    all_turtles.append(new_turtle)

#Process of the Racing
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turlte is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

scr.exitonclick()
