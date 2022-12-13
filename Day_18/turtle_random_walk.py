from turtle import *
import random

t = Turtle()
t.shape("turtle")
t.width(width=10) # or t.pensize(15)
t.speed(2)
directions = [0, 90, 180, 270]
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue",
                "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]


def make_snake (size):
    count = 0
    while count < size:
        t.color(random.choice(colors))
        t.forward(random.randint(20, 50))
        t.setheading(random.choice(directions))
        count += 1

make_snake(50)
