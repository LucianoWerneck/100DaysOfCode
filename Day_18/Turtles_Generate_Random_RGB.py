import turtle as t
import random


t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

directions = [0, 90, 180, 270]
t.pensize(15)
t.speed(2)

for _ in range(200):
    t.color(random_color())
    t.forward(random.randint(30, 60))
    t.setheading(random.choice(directions))

