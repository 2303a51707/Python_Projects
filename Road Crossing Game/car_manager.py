import random
from turtle import Turtle

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT=10

class CarManager:
    def __init__(self, car_shapes):
        self.car_shapes = car_shapes
        self.all_cars = []
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.shape(random.choice(self.car_shapes))
        new_car.shapesize(stretch_wid=2, stretch_len=1)
        new_car.penup()
        new_car.goto(300, random.randint(-250, 250))
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    def level_up(self):
        self.car_speed += MOVE_INCREMENT