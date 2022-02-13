import random
import sys

print("ROCK, PAPER, SCISSORS")

wins = 0
losses = 0
ties = 0

while True:  # the main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    while True:  # the player input loop
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        player_move = input()
        if player_move == "q":
            sys.exit()  # quit the program
        if player_move == "r" or player_move == "p" or player_move == "s":
            break
    print(str(player_move) + " versus")

    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print("ROCK")
    elif random_number == 2:
        computer_move = "p"
        print("PAPER")
    elif random_number == 3:
        computer_move = "s"
        print("SCISSORS")

    if player_move == computer_move:
        ties += 1
        print("It's a tie")
    elif player_move == "r" and computer_move == "p":
        losses += 1
        print("You lose!")
    elif player_move == "r" and computer_move == "s":
        wins += 1
        print("You win!")
    elif player_move == "p" and computer_move == "s":
        losses += 1
        print("You lose!")
    elif player_move == "p" and computer_move == "r":
        wins += 1
        print("You win!")
    elif player_move == "s" and computer_move == "p":
        wins += 1
        print("You win!")
    elif player_move == "s" and computer_move == "r":
        losses += 1
        print("You lose!")
