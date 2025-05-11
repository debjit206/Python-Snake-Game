from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")
GAME_OVER_FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.game_score = 0
        self.level = 1
        with open("data.txt") as file:
            self.game_high_score = int(file.read())
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 270)
        self.write(f"Score: {self.game_score}", False, align=ALIGNMENT, font=FONT)
        self.goto(0, 270)
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font=FONT)
        self.goto(200, 270)
        self.write(f"High Score: {self.game_high_score}", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.game_score += 1
        if self.game_score % 10 == 0:
            self.level += 1
        self.update_scoreboard()
        
    def update_level(self):
        self.level += 1
        
    def get_level(self):
        return self.level

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=GAME_OVER_FONT)
        self.goto(0, -30)
        self.write(f"Final Score: {self.game_score} | Level: {self.level}", False, align=ALIGNMENT, font=FONT)

    def update_high_score(self):
        if self.game_score > self.game_high_score:
            self.game_high_score = self.game_score
            with open("data.txt", "w") as file:
                file.write(str(self.game_high_score))
        self.update_scoreboard()
