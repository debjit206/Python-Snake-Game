from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_new_food()
        self.current_color = "blue"

    def create_new_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        # Generate a random bright color for the food
        self.current_color = self.random_color()
        self.color(self.current_color)
        self.speed("fastest")
        x_coordinate = random.randint(-270, 270)
        y_coordinate = random.randint(-270, 270)
        self.goto(x_coordinate, y_coordinate)
    
    def random_color(self):
        """Generate a random bright color."""
        colors = ["red", "blue", "green", "purple", "orange", 
                 "yellow", "pink", "cyan", "magenta", "lime"]
        return random.choice(colors)
    
    def get_current_color(self):
        """Return the current food color."""
        return self.current_color
