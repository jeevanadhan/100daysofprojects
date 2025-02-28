from turtledemo.forest import doit1

THEME_COLOR = "#375362"
from tkinter import *
from tkinter import messagebox
from quiz_brain import *
class QuizInterface:
    def __init__(self,quizbrain:QuizBrain):
        self.quiz=quizbrain
        self.window= Tk()

        self.window.title("quizler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_text=Label(text=f"score:{self.quiz.score}",font=("aerial",15,"bold"),bg=THEME_COLOR,fg="white")
        self.score_text.grid(row=0,column=0,sticky="e")
        self.canvas=Canvas(width=380,height=250,bg="white")
        self.question_text=self.canvas.create_text(200,120,width=350,text="some questions here",font=("Aerial",20,"italic"),fill=THEME_COLOR)
        self.canvas.grid(pady=20)
        true_image=PhotoImage(file="./images/true.png")
        self.tick_button=Button(image=true_image,bg=THEME_COLOR,activebackground=THEME_COLOR,borderwidth=0,command=self.correct_pressed)
        self.tick_button.grid(sticky="w")
        false_image=PhotoImage(file="./images/false.png")
        self.wrong_button=Button(image=false_image,bg=THEME_COLOR,activebackground=THEME_COLOR,borderwidth=0,command=self.wrong_pressed)
        self.wrong_button.grid(row=2,column=0,sticky="e")
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            messagebox.showinfo(title="out of question",message=f"You've completed the quiz \nYour final score: { self.quiz.score}/{self.quiz.question_number}")
            self.tick_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def correct_pressed(self):

        is_right=self.quiz.check_answer("True")
        self.get_feedback(is_right)
    def wrong_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.get_feedback(is_right)
    def get_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)



