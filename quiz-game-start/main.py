from question_model import Question
from data import question_data

question_bank = []
for item in question_data:
    question_text = item['text']
    question_answer = item['answer']

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    

print(question_bank[2].text)
# Iterate over each question
# create new question object 
# Append to new list
