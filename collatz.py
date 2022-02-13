import random


def collatz(number):
    if number % 2 == 0:
        return number//2
    elif number % 2 != 0:
        return 3 * number + 1


print("Enter number")
n = int(input(">"))
while n != 1:
    n = collatz(n)
    print(n)
