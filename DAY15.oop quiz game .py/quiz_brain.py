class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return 1
        else:
            return 0
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer= input(f"Qn{self.question_number} {current_question.text} (True or false)?").lower()
        self.check_answer(user_ans=user_answer,crt_ans=current_question.answer)
    def check_answer(self,crt_ans,user_ans):
        if user_ans.lower()==crt_ans.lower():
            print("you got it right")

            self.score+=1
        else:
            print("that's wrong")
        print(f"correct answer was {crt_ans}")
        print(f"current score {self.score}/{self.question_number}")
