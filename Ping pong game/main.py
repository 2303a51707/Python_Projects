from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from middledotlines import Middle
from score import Score
import time

# Setup screen
screen = Screen()
screen.bgcolor("darkgreen")
screen.title("Ping Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

# Draw court
middle_line = Middle()
middle_line.draw_dotted_line()
middle_line.draw_horizontal_line(y=0, thickness=2)
middle_line.draw_border(width=800, height=600, thickness=4)

# Create paddles and ball
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Score()

# Controls
screen.listen()
screen.onkey(r_paddle.go_up, "o")
screen.onkey(r_paddle.go_down, "l")
screen.onkey(l_paddle.go_up, "q")
screen.onkey(l_paddle.go_down, "a")

# Show instructions
instruction = Turtle()
instruction.hideturtle()
instruction.color("white")
instruction.penup()
instruction.goto(0, 0)
instruction.write("🎮 Controls:\nLeft: Q/A | Right: O/L\nPress SPACE to start!", align="center", font=("Courier", 16, "bold"))

# Game start function
def start_game():
    instruction.clear()
    time.sleep(1)  # Delay before game starts
    game_on = True
    while game_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Bounce off top and bottom
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Paddle collisions
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
           (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        # Missed by right paddle
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        # Missed by left paddle
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()

        # Game over
        if scoreboard.l_score == 5 or scoreboard.r_score == 5:
            game_on = False
            winner = "Left Player" if scoreboard.l_score == 5 else "Right Player"
            game_over = Turtle()
            game_over.hideturtle()
            game_over.color("yellow")
            game_over.penup()
            game_over.goto(0, 0)
            game_over.write(f"🏆 {winner} Wins!\nGame Over", align="center", font=("Courier", 24, "bold"))

# Trigger game start on spacebar
screen.onkey(start_game, "space")

# Exit on click
screen.exitonclick() 