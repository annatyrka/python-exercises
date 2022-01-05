import re


def palindrome(message):
    forwards = "".join(re.findall(r'[a-z]+', message.lower()))
    backwards = forwards[::-1]
    return forwards == backwards


print(palindrome("iannai"))
