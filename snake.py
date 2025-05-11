from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the initial snake with 3 segments."""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position, color=None):
        """Add a new segment to the snake."""
        new_segment = Turtle("square")
        new_segment.penup()
        if color:
            new_segment.color(color)
        else:
            new_segment.color("white")  # Default color
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self, color=None):
        """Add a new segment to the snake when it eats food."""
        self.add_segment(self.segments[-1].position(), color)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_coordinate = self.segments[i - 1].xcor()
            y_coordinate = self.segments[i - 1].ycor()
            self.segments[i].goto(x_coordinate, y_coordinate)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def change_color(self, color):
        """Change the color of the snake's head and all segments."""
        for segment in self.segments:
            segment.color(color)
