import random
guess = ''
assert guess != 'heads' and guess != 'tails'
while guess not in ('heads', 'tails'):
    print('Gues the coin toss! Enter heads or tails: ')
    guess = input()
toss = random.choice(['heads', 'tails'])  # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
