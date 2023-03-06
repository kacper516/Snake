from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 22, 'normal')


class Scoreboard(Turtle):
    """This is a simple class for scoreboard in my game"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.print_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.print_score()

    def print_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)  # center
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
