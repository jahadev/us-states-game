import pandas
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=700, height=600)
turtle = Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("U.S. States Game")

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
missing_states = []

while len(guessed_states) < 50:
  answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
  
  if answer == "Exit":
    for state in all_states:
      if state not in guessed_states:
        missing_states.append(state)
    learn_data = pandas.DataFrame(missing_states)
    learn_data.to_csv("learn.csv")
    break
  
  if answer in all_states:
    guessed_states.append(answer)
    t = Turtle()
    t.hideturtle()
    t.penup()
    answer_row = data[data.state == answer]
    t.goto(int(answer_row.x), int(answer_row.y))
    t.write(answer)


