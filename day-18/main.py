from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
# tim.color("red")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.right(angle)
        tim.forward(100)

def random_walk():
    tim.forward()

for _ in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(_)

    # tim.forward(4)
    # tim.pendown()

# import heroes
# print(heroes.gen())


screen = Screen()
screen.exitonclick()
