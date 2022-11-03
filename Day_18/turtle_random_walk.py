from turtle import Turtle
import random

tim = Turtle()
tim.shape("turtle")
tim.width(width=10)
tim.speed(1)
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue",
                "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]


def make_snake (size):
    count = 0
    while count < size:
        tim.color(random.choice(colors))
        tim.forward(random.randint(20, 50))
        tim.setheading(random.choice([90, 180, 270, 360]))
        count += 1

make_snake(50)
