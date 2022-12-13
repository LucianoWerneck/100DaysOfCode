import turtle as t
import random

t.speed(15)
t.pensize(1.5)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for i in range (100):
        t.color(random_color())
        t.circle(100)
        t.left(5)

