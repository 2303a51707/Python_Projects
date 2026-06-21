import time
from turtle import Turtle

class Middle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()

    def draw_dotted_line(self, segments=15, dot_length=20, gap=20, delay=0.05):
        self.goto(0, -300)
        self.setheading(90)
        for _ in range(segments):
            self.pendown()
            self.forward(dot_length)
            self.penup()
            self.forward(gap)
            time.sleep(delay)

    def draw_horizontal_line(self, y=0, thickness=2):
        line = Turtle()
        line.hideturtle()
        line.color("white")
        line.pensize(thickness)
        line.penup()
        line.goto(-400, y)
        line.pendown()
        line.goto(400, y)

    def draw_border(self, width=800, height=600, thickness=3):
        border = Turtle()
        border.hideturtle()
        border.color("white")
        border.pensize(thickness)
        border.penup()
        border.goto(-width//2, -height//2)
        border.pendown()
        for _ in range(2):
            border.forward(width)
            border.left(90)
            border.forward(height)
            border.left(90)