from turtle import Screen, Turtle
screen = Screen()

# Creating the self
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        #Setting its speed as zero, it moves only when key is pressed
        self.speed(0)
        #Setting shape, color, and size
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1.2)
        self.penup()
        #The paddle is left-centered initially
        self.goto(position)

    # Function to move paddle up
    def go_up(self):
         new_y = self.ycor() + 20
         self.goto(self.xcor(), new_y)
    # Function to move the self down
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
    # Command keys
    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")