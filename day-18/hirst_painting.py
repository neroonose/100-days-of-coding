import turtle as t
from turtle import Screen
import random

t.colormode(255)
tim = t.Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()
color_list = [(131, 165, 204), (220, 149, 109), (30, 41, 62), (200, 134, 146),
              (166, 58, 48), (141, 184, 162), (41, 104, 153), (236, 213, 95),
              (149, 60, 67), (215, 82, 72), (235, 165, 157), (52, 112, 91),
              (33, 60, 55), (171, 29, 32), (156, 33, 30), (52, 44, 49), (229, 162, 166),
              (170, 188, 220), (17, 96, 71), (57, 51, 48), (30, 60, 110), (182, 103, 113),
              (108, 126, 158), (175, 200, 188), (34, 150, 210), (65, 66, 57)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    color = random.choice(color_list)
    tim.dot(20, color)
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

