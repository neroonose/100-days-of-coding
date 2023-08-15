STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.penup()
        self.starting_postion()
    
    def go_up(self):
        new_position = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_position)

    def starting_postion(self):
        self.goto(STARTING_POSITION)

    def end_point(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False
