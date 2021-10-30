from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz")
print(f"Your final score is: {quiz.score} / {quiz.question_number}")


# class User:
#     def __init__(self, user_id, user_name):
#         self.id = user_id
#         self.user_name = user_name
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User("001", "Ray")
# user_2 = User("002", "Mond")
#
# user_1.follow(user_2)
#
# print(user_1.followers)
# print(user_1.following)
# print(user_2.following)
# print(user_2.followers)