from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup screen
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(n=0)
my_screen.listen()

# Initialize game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Setup controls
my_screen.onkey(fun=snake.up, key="Up")
my_screen.onkey(fun=snake.down, key="Down")
my_screen.onkey(fun=snake.left, key="Left")
my_screen.onkey(fun=snake.right, key="Right")
my_screen.onkey(fun=snake.up, key="w")
my_screen.onkey(fun=snake.down, key="s")
my_screen.onkey(fun=snake.left, key="a")
my_screen.onkey(fun=snake.right, key="d")

# Game variables
game_on = True
base_speed = 0.13
current_speed = base_speed
pause = False

# Pause function
def toggle_pause():
    global pause
    pause = not pause
    
my_screen.onkey(fun=toggle_pause, key="space")

# Game loop
while game_on:
    my_screen.update()
    
    # Handle pause
    if pause:
        my_screen.update()
        scoreboard.goto(0, 0)
        scoreboard.write("PAUSED - Press SPACE to continue", align="center", font=("Courier", 16, "normal"))
        time.sleep(0.5)
        my_screen.update()
        while pause:
            my_screen.update()
            time.sleep(0.1)
        scoreboard.update_scoreboard()
        continue
    
    # Calculate speed based on level
    current_level = scoreboard.get_level()
    current_speed = max(0.03, base_speed - (current_level - 1) * 0.01)
    
    time.sleep(current_speed)
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.create_new_food()
        snake.extend_snake()
        scoreboard.update_score()
    
    # Detect collision with wall
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or 
        snake.head.ycor() > 290 or snake.head.ycor() < -290):
        game_on = False
        scoreboard.update_high_score()
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.update_high_score()
            scoreboard.game_over()

my_screen.exitonclick()
