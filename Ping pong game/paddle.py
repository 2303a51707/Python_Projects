from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        screen = Screen()
        screen.register_shape("redpaddle.gif")  # Register your custom GIF

        self.shape("redpaddle.gif")  # Apply the image as paddle shape
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 40
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        if new_y > -250:
            self.goto(self.xcor(), new_y)