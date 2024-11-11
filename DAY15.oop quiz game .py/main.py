from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
print(r"""  
     / _ \  | | | | |_ _| |__  /  
    | | | | | | | |  | |    / /   
    | |_| | | |_| |  | |   / /_   
     \__\_\  \___/ _|___| /____|_ 
    |_   _| |_ _| |  \/  | | ____|
      | |    | |  | |\/| | |  _|  
      | |    | |  | |  | | | |___ 
      |_|   |___| |_|  |_| |_____|""")
question_bank=[]
for i in range(len(question_data)):
    new_question=Question(question_data[i]["question"],question_data[i]["correct_answer"])
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_question():
    quiz.next_question()

print("congratulate you completed the game")
print(f"you final score was {quiz.score}/{quiz.question_number}")