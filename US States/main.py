import turtle
import pandas as pd

screen=turtle.Screen()
screen.title("US States")
image=("blank_states_img.gif")
screen.addshape(image)
turtle.shape(image)

data=pd.read_csv("50_states.csv")
all_states=data.state.to_list()
gussed_states=[]


while len(gussed_states) < 50:
    answer_state=screen.textinput(title=f"{len(gussed_states)}/50 States Correct",prompt="what's another state's name?").title()
    
    if answer_state=="Exit":
        missing_states=[state for state in all_states if state not in gussed_states]
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        
        break

    if answer_state in all_states:
        gussed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)
    
screen.exitonclick()



