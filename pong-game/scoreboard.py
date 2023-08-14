from turtle import Turtle
FONT = ("Courier", 40, "normal")

class ScoreBoard(Turtle):

    def __init__ (self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.scores = 0
        self.goto(position)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.scores}", font=FONT)

    def increase_score(self):
        self.scores +=1
        self.clear()
        self.update_scoreboard()