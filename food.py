from turtle import Turtle
import random


class Food(Turtle):
    """This is a simple class for food"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 20px*0.5=10px
        self.penup()
        self.create_food()

    def create_food(self):
        random_x = random.randrange(-280, 280, 20)  # size of screen
        random_y = random.randrange(-280, 280, 20)  # size of screen
        self.goto(random_x, random_y)

