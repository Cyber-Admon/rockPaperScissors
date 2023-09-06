import random

# The possible moves in the game.
moves = ["rock", "paper", "scissors"]


def play_round():

    user_move = input("Choose your move: rock, paper, or scissors: ")

    computer_move = random.choice(moves)

    print("You chose:", user_move)
    print("Computer chose:", computer_move)

    if user_move == computer_move:
        print("It's a tie!")
    elif user_move == "rock":
        if computer_move == "scissors":
            print("You win!")
        else:
            print("Computer wins!")
    elif user_move == "paper":
        if computer_move == "rock":
            print("You win!")
        else:
            print("Computer wins!")
    elif user_move == "scissors":
        if computer_move == "paper":
            print("You win!")
        else:
            print("Computer wins!")


while True:
    play_round()
    answer = input("Do you want to play again? (Y/N): ")

    if answer.lower() == "n":
        print("Nice Playing with you")
        break
