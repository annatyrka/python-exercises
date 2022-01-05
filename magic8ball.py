import random
import sys

# user ask a yes-no question  and it returns possible answers

answers = ["It is certain.", "It is decidedly so.", "Without a doubt.",
           "Yes – definitely.", "You may rely on it.", "As I see it, yes.",
           "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
           "Reply hazy, try again.", "Ask again later.",
           "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
           "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

print("Ask your question. Press q to quit")


for i in range(len(answers)):
    question = input()
    if question == "q":
        sys.exit()
    print(answers[random.randint(1, len(answers))])
