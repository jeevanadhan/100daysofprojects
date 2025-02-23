from inspect import Traceback
from tkinter import *
import pandas,random

BACKGROUND_COLOR = "#B1DDC6"
window= Tk()
window.title("flash card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

correct_word={}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except (FileNotFoundError,pandas.errors.EmptyDataError):
    original_data= pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global flip_timer,current_card
    if flip_timer:
        window.after_cancel(flip_timer)
    canvas.itemconfig(front_card,image=front_img)
    canvas.itemconfig(title_text, text="french",fill="black")
    current_card=random.choice(to_learn)
    canvas.itemconfig(word_text,text=current_card["French"],fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(front_card,image=back_img)
    canvas.itemconfig(title_text,text="English",fill="White")
    canvas.itemconfig(word_text,text=current_card["English"],fill="white")
def is_known():
    to_learn.remove(current_card)
    print(f"{len(to_learn)} words to learn")
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


flip_timer=window.after(4000,func=flip_card)

canvas=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
front_img=PhotoImage(file="./images/card_front.png")
back_img=PhotoImage(file="./images/card_back.png")
current_card = random.choice(to_learn)

front_card=canvas.create_image(400,262,image=front_img)
canvas.grid(row=2,column=2)

#BUTTONS
      # tick image button
tick_image=PhotoImage(file="./images/right.png")
button=Button(image=tick_image,highlightthickness=0,activebackground=BACKGROUND_COLOR,borderwidth=0,command=is_known)
button.grid(row=3,column=2,sticky="e",padx=(0,130))
        # wrong image button
wrong_image=PhotoImage(file="./images/wrong.png")
button=Button(image=wrong_image,highlightthickness=0,activebackground=BACKGROUND_COLOR,borderwidth=0,command=next_card)
button.grid(row=3,column=2,sticky="w",padx=(130,0))


title_text=canvas.create_text(400,150,text="french",font=("Aerial",40,"italic"),fill="black")
word_text=canvas.create_text(400,300,text=current_card["French"],font=("Aerial",55,"bold"),fill="black")
canvas.bind()
window.mainloop()



