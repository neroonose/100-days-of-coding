from question_model import Question
from data import question_data


question_bank = []

for i in question_data:
    text = i['text']
    answer = i['answer']
    new_question = Question(q_text = text, q_answer = answer)
    question_bank.append(new_question)

print(question_bank)