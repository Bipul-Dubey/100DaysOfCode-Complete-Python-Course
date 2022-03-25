import turtle,pandas

screen=turtle.Screen()
screen.title("India States Game")
image="India States Map.gif"
screen.setup(height=800)
screen.addshape(image)
turtle.shape(image)


data=pandas.read_csv("29_states.csv")
all_states=data.state.to_list()
guess_states=[]
guess=0
while len(guess_states)<29 and guess<=29:
    answer_state=screen.textinput(title=f"{guess}/29 States Correct",prompt="Name of Indian State?? ").title()

    if answer_state=='Exit':
        missing_states=[state for state in all_states if state not in guess_states]
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("Indian_State_to_learn.csv")
        break

    if answer_state in all_states:
        guess_states.append(answer_state)
        t=turtle.Turtle()
        t.ht()
        t.penup()
        t.color("red")
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
        guess+=1
