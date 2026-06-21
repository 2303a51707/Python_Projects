from turtle import Turtle


message = Turtle()
message.hideturtle()
message.color("white")
message.penup()
message.goto(0, 0)
message.write("GAME OVER", align="center", font=("Courier", 24, "bold"))