# Python For Beginners | Chapter 1: Rock, Paper, Scissors | Class 8. Refactoring and Nested If Statements
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Refactoring the Rock Paper Scissors Game
# -----------------------------------------------------------------------

player = "rock"
computer = "scissors"

if player == computer:
    print("Draw")

else:

    if player == "rock":
        if computer == "scissors":
            print("Player wins")
        else:
            print("Computer wins")

    elif player == "paper":
        if computer == "rock":
            print("Player wins")
        else:
            print("Computer wins")

    elif player == "scissors":
        if computer == "paper":
            print("Player wins")
        else:
            print("Computer wins")

# -----------------------------------------------------------------------
# B. Using a dictionary to refactor the Rock Paper Scissors Game
# -----------------------------------------------------------------------

game_rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def determine_winner(player, computer):

    if player == computer:
        return "Draw"

    if game_rules[player] == computer:
        return "Player wins"

    return "Computer wins"

r1 = determine_winner("rock", "scissors")
print(r1)

r2 = determine_winner("paper", "rock")
print(r2)

r3 = determine_winner("scissors", "paper")
print(r3)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------