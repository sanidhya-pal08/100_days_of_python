# ask the questions 
# check if the answer was correct
# checking if we are at the end of the code


class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.length=len(question_list)
        self.score=0

    def still_has_questions(self):
        return self.question_number<self.length
    
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        current_answer=input(f"Q.{self.question_number} : {current_question.text} (True/False)")
        self.check_answer(current_answer,current_question.answer)
    
    def check_answer(self,current_answer,actual_answer):
        number=self.question_number-1
        if(current_answer.lower()==actual_answer.lower()):
            self.score+=1
            print(f"correct answer \nYour score is now {self.score}")
        else:
            print(f"wrong answer\nYour score is now {self.score}")