
import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess the Names of Indian States")
screen.setup(width=500, height=500)
image = 'blank_map.gif'
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

# function to get the coordinates of states.
# click on the point you want to display state name and then the x and y coordinates will be printed in console
#
# def print_xy(x, y):
#     print(f"{x}, {y}")
#
# screen.onscreenclick(print_xy)

data = pandas.read_csv('Indian_States_Coordinates.csv')
states = data['State'].to_list()

correct_guesses = []

while len(correct_guesses) < 29:

    answer = screen.textinput(title=f'Guess the State {len(correct_guesses)}/29', prompt='Enter Name or "Exit" to Quit')
    answer = answer.title()

    if answer == "Exit":
        missing_states = [n for n in states if n not in correct_guesses]
        missing_guess = {
            'State': missing_states
        }
        pandas.DataFrame(missing_guess).to_csv('states_to_learn.csv', index=False)
        break

    if answer in states:
        state = data[data.State == answer]
        x_ = int(state.x)
        y_ = int(state.y)
        correct_guesses.append(answer)
        pen.goto(x=x_, y=y_)
        pen.write(f"{answer}", font=('Arial', 8, 'normal'))

screen.clear()
pen.goto(0, 0)
end_text = ""
score = len(correct_guesses)
if score == 29:
    end_text = 'You Guessed Them All Correctly'
elif score >= 20:
    end_text = f"Good Work: {score}/29"
elif score >= 15:
    end_text = f"Average Performance: {score}/29"
else:
    end_text = f"Poor Performance: {score}/29"

pen.write(f"{end_text}", align='center', font=("Arial", 22, 'normal'))

turtle.mainloop()
