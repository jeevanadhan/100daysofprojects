from tkinter import *
import math
from turtledemo.penrose import start

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET. ------------------------------- #
def time_reset():
    global timer,reps
    reps=0
    window.after_cancel(timer)


    timer_label.config(text="TIMER",fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1
    if reps%8==0:
        timer_label.config(text="LONG BREAK",fg=RED)
        count_down(LONG_BREAK_MIN*60)

    elif reps%2==0:
        timer_label.config(text="BREAK",fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    elif reps%2==1:
        timer_label.config(text="WORK",fg=RED)
        count_down(WORK_MIN*60)


    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec="0" + str(count_sec)

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        work_session=math.floor(reps/2)
        marks=""
        for _ in range(work_session):
            marks+="✔"
            check_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("pomodoro technique")
window.config(padx=50,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)

photoimage=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=photoimage)

timer_text=canvas.create_text(103,130,fill="white",text="00:00",font=(FONT_NAME,20,"bold"))
canvas.grid(column=1,row=1)

start_button=Button(text="start",highlightthickness=0,borderwidth=0,command=start_timer)
start_button.grid(column=0,row=2)

timer_label=Label(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
timer_label.grid(column=1,row=0)

check_label=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,10,"bold"))
check_label.grid(column=1,row=4)

reset_button=Button(text="reset",highlightthickness=0,borderwidth=0,command=time_reset)
reset_button.grid(column=2,row=2)

window.mainloop()
