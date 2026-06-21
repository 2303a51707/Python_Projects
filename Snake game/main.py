from turtle import Screen,Turtle as s
from snake import Snake
from food import Food
from Score import score

import time


screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake=Snake()
food=Food()
score=score()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



    
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        
        
    if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        score.reset()
        snake.reset()
         
         
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


    

screen.exitonclick()
    
    
        
        
    

