import turtle as t
import random

tim = t.Turtle()    
t.colormode(255)

tim.pensize(6)
tim.speed(3)
tim.shape("turtle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]

for _ in range(100):
    # tim.color(random.choice(colours))
    # tim.random_color()
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


# screen = Screen()
# screen.exitonclick()