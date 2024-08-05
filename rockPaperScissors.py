"""
Purpose: Play rock-paper-scissors against the computer!
"""

import random

def winner(player1choice, player2choice):
    """Determine the winner of a round of rock, paper, scissors.
    Rock beats scissors, scissors beat paper, and paper beats rock.

    Parameters:
        player1choice, player2choice: 'rock', 'paper', or 'scissors'

    Return value: 1 if player 1 wins, 
                  2 if player 2 wins,
                  0 if it's a tie
    """
    if player1choice == player2choice:
        return 0
    elif (player1choice == 'rock' and player2choice == 'scissors') or \
         (player1choice == 'scissors' and player2choice == 'paper') or \
         (player1choice == 'paper' and player2choice == 'rock'):
        return 1
    else:
        return 2

def randomChoice():
    """Returns a random choice from 'rock', 'paper', or 'scissors'."""
    return random.choice(['rock', 'paper', 'scissors'])

def getChoice(playerName):
    """Prompt for a choice until the player enters "rock", "paper", 
    or "scissors".

    Parameter: playerName, a string
    Return value: a string, either "rock", "paper", or "scissors"
    """
    choice = input("{}, what is your choice? (rock, paper, or scissors): ".format(playerName)).lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Please enter 'rock', 'paper', or 'scissors': ").lower()
    return choice

def playRound(playerName):
    """Play one round of Rock-Paper-Scissors.

    Parameters: playerName, a string

    Return value: 1 if player 1 won, 
                  2 if player 2 won,
                  0 if it was a tie
    """
    human = getChoice(playerName)
    computer = randomChoice()
    print("The computer chose {}".format(computer))

    whoWon = winner(human, computer)
    
    if whoWon == 1:
        print("{}, you win!".format(playerName))
    elif whoWon == 2:
        print("The computer won!")
    else:
        print("It's a tie!")

    return whoWon

def playGame():
    """Let the user play multiple rounds of Rock-Paper-Scissors against the 
       computer. At the end, report how many rounds were won by the user
       and the computer, and who won the tournament.
    """
    print("Let's play Rock-Paper-Scissors!")
    name = input("What's your name? ")

    human_wins = 0
    computer_wins = 0

    rounds = int(input("How many rounds would you like to play? "))

    for _ in range(rounds):
        result = playRound(name)
        if result == 1:
            human_wins += 1
        elif result == 2:
            computer_wins += 1

    print("\nGame Over!")
    print("You won {} rounds.".format(human_wins))
    print("The computer won {} rounds.".format(computer_wins))

    if human_wins > computer_wins:
        print("Congratulations, you won the tournament!")
    elif computer_wins > human_wins:
        print("The computer won the tournament!")
    else:
        print("The tournament ended in a tie!")

if __name__ == '__main__':
    playGame()
