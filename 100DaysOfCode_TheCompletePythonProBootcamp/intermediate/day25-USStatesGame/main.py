import turtle
import pandas

image = "./blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)


states = pandas.read_csv("50_states.csv")

# Convert states column into an iterable list
state_column = states.state
states_list = state_column.to_list()

score = 0 # keep track of a user score

states_guessed =[]  #  Add guessed states here. If a guessed state is already here - do not add score

game_over = False

def write_on_map(user_input, x_cor, y_cor):
    place_state = turtle.Turtle()
    place_state.shape("circle")
    place_state.shapesize(0.4, 0.4)
    place_state.pu()
    place_state.goto(x_cor,y_cor)
    place_state.write(arg = f"{user_input}", align = "center", font = ('Fira Code Nerd Font Mono', 12, 'normal'))

def states_to_learn():

    states_to_learn = []

    for s in states_list:
        if not s in states_guessed:
            states_to_learn.append(s)
            
    states_to_learn_dict = {"States to learn": states_to_learn}
    data = pandas.DataFrame(states_to_learn_dict)
    data.to_csv("states_to_learn.csv")

while not game_over:
    try:
        answer_state = screen.textinput(title="Guess the state", prompt=f"Enter a state's name ({score}/50)").title() # prompt user
    except AttributeError:
        print("Cancelling")
        states_to_learn()
        game_over= True
    else:
        if answer_state in states_guessed :
            print("You already guessed it")
        elif  answer_state in states_list:
            score += 1
            state_info = (states[states.state == f"{answer_state}"])
            write_on_map(answer_state,int(state_info.x.iloc[0]), int(state_info.y.iloc[0]))
            states_guessed.append(answer_state)
        elif answer_state == "Exit":
            print("Exiting")
            states_to_learn()
            game_over= True
        else:
            print("WRONG!")

        if score == 50:
            game_over = True
            print("Congrats! You guessed them all!")

