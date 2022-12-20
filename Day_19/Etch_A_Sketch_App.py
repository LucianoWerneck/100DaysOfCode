from turtle import Turtle, Screen

t = Turtle()
scr = Screen()


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def move_counterclockwise():
    t.right(10)


def move_clockwise():
    t.left(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


scr.listen()
scr.onkey(move_forwards, "w")
scr.onkey(move_backwards, "s")
scr.onkey(move_counterclockwise, "a")
scr.onkey(move_clockwise, "d")
scr.onkey(clear, "c")

scr.exitonclick()
