import re


def palindrome(message):
    print("Enter your text")
    forwards = "".join(re.findall(r'[a-z]+', message.lower()))
    backwards = forwards[::-1]
    return forwards == backwards


print(palindrome("Anna re"))
