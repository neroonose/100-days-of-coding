import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
# tim.shape("turtle")

tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for i in range(0, 360, 10):
    tim.color(random_color())
    tim.setheading(i)
    tim.circle(100)
