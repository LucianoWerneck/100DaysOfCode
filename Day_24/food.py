from turtle import Turtle
import random


class Food(Turtle):

    def color_food_random(self):
        colors = ["red", "blue", "green", "cyan", "yellow", "pink", "purple", "gold", "magenta"]
        self.color(random.choice(colors))

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.9, stretch_wid=0.9)
        self.speed("fast")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.color_food_random()
        self.goto(random_x, random_y)
