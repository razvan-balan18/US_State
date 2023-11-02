import turtle
import pandas

screen = turtle.Screen()
screen.setup(730, 500)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50", prompt="Guess a name").title()
    states_to_learn = []
    if answer_state == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]
        df = pandas.DataFrame(states_to_learn, columns=['states_to_learn'])
        csv_data = df.to_csv("states")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)

