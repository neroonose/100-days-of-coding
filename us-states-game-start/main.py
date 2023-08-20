import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us-states-game-start\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("us-states-game-start\\50_states.csv")
states = data.state.to_list()
score = 0
correct_guesses = []
while len(correct_guesses) < 50:
    answer = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name?")
    answer_state = answer.title()
    if answer_state == "Exit":
        break
    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        score += 1
        correct_guesses.append(answer_state)
missing_states = [state for state in states if state not in correct_guesses]


df = pandas.DataFrame(missing_states)
df.to_csv("us-states-game-start\\states_to_learn_csv")
