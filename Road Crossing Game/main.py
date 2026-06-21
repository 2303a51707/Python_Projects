import pygame
from turtle import Screen,Turtle
import time
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("vehicles_sound.mp3")  
pygame.mixer.music.set_volume(0.7)             
pygame.mixer.music.play(-1)                    


screen = Screen()
screen.title("Crossing Road Game")
screen.bgpic("roadbg.gif")                     
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard=Scoreboard()

player=Player()
screen.listen()
screen.onkey(player.move_player,"Up")
screen.onkey(player.move_back,"Down")



CARS = ["white.gif","red.gif","blue.gif","green.gif","yellow.gif","blackk.gif"]
for car_shape in CARS:
    screen.register_shape(car_shape)


car_manager = CarManager(CARS)


car_spawn_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_spawn_counter += 1
    if car_spawn_counter % 6 == 0:
        car_manager.create_car()

    car_manager.move_cars()
    
    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_is_on = False
            message = Turtle()
            message.hideturtle()
            message.color("white")
            message.penup()
            message.goto(0, 0)
            message.write("GAME OVER", align="center", font=("Courier", 24, "bold"))
            
    

            
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
            

screen.exitonclick()