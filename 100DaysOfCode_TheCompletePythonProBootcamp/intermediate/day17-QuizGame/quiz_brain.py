class QuizBrain:
    
    def __init__(self, question_list):
        
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        
    def next_question(self):
        
        quiz_is_going = True
        
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        ask = input(f"Q.{self.question_number}. {current_question.statement}. True/False: ")
        self.check_answer(ask, current_question.answer)
    
    def still_has_questions(self):
        
        return self.question_number < len(self.question_list)

    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}") 
        
        print(f"Your current score is {self.score}/{self.question_number}\n")
        
    def finale(self):
        
        print(f"You finished the quiz.\nYour finale score is {self.score}/{len(self.question_list)}")
        
        
    