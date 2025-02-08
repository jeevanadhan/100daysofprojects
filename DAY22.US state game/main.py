import turtle,pandas
screen=turtle.Screen()
img="blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
with open("50_states.csv") as file:
    data = pandas.read_csv(file)
    data_dict = data.to_dict()

    state_list = data["state"].to_list()
game_over=False
guessed=0
guessed_states=[]
while not game_over:
    user_answer=screen.textinput(title=f"{guessed}/50  Guess the state",prompt="whats the another state name?")
    if user_answer is None:
        break
    elif user_answer=="exit":
        break


    if user_answer.title() in state_list:
        guessed_states.append(user_answer)
        state_index = state_list.index(user_answer.title())
        xcor=data_dict["x"][state_index]
        ycor=data_dict["y"][state_index]
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(xcor,ycor)
        t.write(arg=str(user_answer),font=("Arial", 7, "bold"))
        guessed+=1
        state_list.remove(state_list[state_index])
    if guessed>=50:

        game_over =True
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(0,0)
        t.write(arg="YOU WON",align="center",font=("Aerial",24,"bold"))
df=pandas.DataFrame(state_list)
df.to_csv("states_to_learn.csv")
