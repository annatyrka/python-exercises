import time
import random
import re

number_of_questions = 11
correct_answers = 0

for question_number in range(1, number_of_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    for i in range(1, 4):
        try:
            answer = int(input('#%s: %s * %s ' %
                               (question_number, num1, num2)))
            if answer == num1 * num2:
                print("Correct!")
                time.sleep(1)
                correct_answers += 1
                break
            if answer != num1 * num2:
                if i != 3:
                    print("Try again, attempt %s" % (i+1))
                else:
                    print("This time you lost :(")
        except ValueError:
            print('Invalid answer')
print('Score: %s, incorrect answers %s' %
      (correct_answers, (number_of_questions - correct_answers)))
