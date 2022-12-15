
#extracting rgb color palette from image
'''import colorgram as cg

rgb_colors = []
colors = cg.extract("image.jpg", 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)'''

palette_colors = (224, 159, 68), (32, 105, 161), (230, 213, 95), (184, 45, 84), (216, 140, 172), (136, 105, 61),\
                (115, 186, 210), (211, 79, 100), (152, 26, 65), (118, 188, 154), (26, 55, 125), (188, 166, 44), \
                (21, 180, 154), (144, 208, 226), (107, 109, 189), (232, 90, 51), (24, 138, 89), (228, 167, 188), \
                (30, 160, 204), (80, 42, 31), (96, 50, 39), (24, 41, 76), (28, 86, 90), (27, 86, 83), (155, 212, 197)
import random
import turtle

turtle.colormode(255)
t = turtle.Turtle()
s = turtle.Screen()
t.penup()
t.hideturtle()
t.speed(0)
t.setpos(-200, -200)

for m in range(10):
    for n in range(10):
        t.dot(20, random.choice(palette_colors))
        t.forward(50)
    t.setx(-200)
    t.sety(t.ycor()+50)

s.exitonclick()