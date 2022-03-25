import turtle,pandas

screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

## to get the coordinates (x,y)
# def get_more_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_more_click_coor)
# turtle.mainloop()

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guess_states=[]
guess=0
while len(guess_states)<50 and guess<=50:
    answer_state=screen.textinput(title=f"{guess}/50 States Correct",prompt="Name of U.S. State?? ")
    answer_state=answer_state.title()

    if answer_state=='Exit':
        missing_states=[state for state in all_states if state not in guess_states] # using list comprehension
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("State_to_learn.csv")
        break

    # if answer_states present in 50_states or not
    if answer_state in all_states:
        guess_states.append(answer_state)
        t=turtle.Turtle()
        t.ht()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
        guess+=1