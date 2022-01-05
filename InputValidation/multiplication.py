import pyinputplus as pyip
import random
import time

number_of_questions = 10
correct_answers = 0

for question_no in range(number_of_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (question_no, num1, num2)
    try:
        # Right answers are handled by allowRegex
        # Wrong answers are handled by blockRegex, with a custom message.

        pyip.inputStr(prompt, allowRegexes=['^%s$' % (
            num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print("Correct")
        correct_answers += 1

    time.sleep(1)  # Brief pause to let user see the result.
print('Score: %s / %s' % (correct_answers, number_of_questions))
