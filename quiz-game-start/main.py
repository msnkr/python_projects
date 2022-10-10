from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    new_question = Question(item['question'], item['correct_answer'])
    question_bank.append(new_question)

question = QuizBrain(question_bank)
while question.still_has_questions():
    question.next_question()

print('You have completed the quiz.')
print(f'Your final score is {question.score}/{question.question_number}')