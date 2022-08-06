class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        
    def still_has_question(self):
        question_list_size = len(self.question_list)
        return self.question_number < question_list_size
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct")
            self.score += 1
        else:
            print("Wrong")
        print(f"The answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        correct_answer = current_question.answer
        self.check_answer(user_answer, correct_answer)
        