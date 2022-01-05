# 1. 35 different quizzes
# 2. 50 multiple-choice questions each in random order
# 3. 1 correct answer, 3 wrong answers in random order
# 4. Writes the quizzes to 35 files
# 5. Writes the answer keys to 35 files

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


for quiz_number in range(3):
    quize_file = open(f"USAcapitals{quiz_number +1}.txt", "w")
    answers_file = open(f"USAcapitals_answers{quiz_number +1}.txt", "w")
    n = 1
    states = list(capitals.keys())
    random.shuffle(states)
    quize_file.write("Name: \nDate: \n\n")
    for state in states:
        quize_file.write(
            str(n) + ": " + "What is the capital of: " + state + "\n")
        # Get right and wrong answers
        correct_answer = capitals[state]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)
        for i in range(4):
            quize_file.write(f"   {'ABCD'[i]}. {answer_options[i]}\n")
            quize_file.write("\n")

        answers_file.write(str(n) + " " + correct_answer + "\n")
        n += 1
    quize_file.close()
    answers_file.close()
