# create rock, paper, scissors game, The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# The computer will randomly choose one of the three options.
# A winner will be decided according to the following rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# The player should be asked if they want to play again. If they do, the game will start again.
# If they don't, the program will stop.
# The program should also display some basic instructions and rules for the user.
# The program should also display the number of wins and losses the player has against the computer.
# The program should also display the number of wins and losses the player has against the computer.

import random

print("Welcome to Rock, Paper, Scissors Game!")
print("Instructions: ")
print("Rock beats scissors")
print("Scissors beats paper")
print("Paper beats rock")
print("If you want to quit the game, please type 'quit'.")

player_wins = 0
computer_wins = 0

while True:
    print("")
    user_input = input("Please enter your choice: ").lower()
    if user_input == "quit":
        break
    if user_input not in ["rock", "paper", "scissors"]:
        print("Please enter a valid option.")
        continue

    random_num = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    if random_num == 0:
        computer = "rock"
    elif random_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print("Computer picked", computer + ".")

    if user_input == computer:
        print("It's a tie!")
    elif user_input == "rock":
        if computer == "scissors":
            print("You win!")
            player_wins += 1
        else:
            print("You lose!")
            computer_wins += 1
    elif user_input == "paper":
        if computer == "rock":
            print("You win!")
            player_wins += 1
        else:
            print("You lose!")
            computer_wins += 1
    elif user_input == "scissors":
        if computer == "paper":
            print("You win!")
            player_wins += 1
        else:
            print("You lose!")
            computer_wins += 1
    else:
        print("Please enter a valid option.")

print("You won", player_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Goodbye!")