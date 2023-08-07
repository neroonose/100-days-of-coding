from turtle import Turtle, Screen
import random

is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -100, -50, 0, 50, 100]
turtles = []

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-210, y=y_positions[index])
    turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(1, 10)
        # global new_turtle
        turtle.forward(rand_distance)
        # if turtles.position(210):
        #     is_game_on = False




screen.exitonclick()
