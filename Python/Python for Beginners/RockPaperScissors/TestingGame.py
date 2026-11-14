# Python For Beginners | Chapter 1: Rock, Paper, Scissors | Class 10. Testing Game
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Test all possible combinations
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


# Test cases

print(determine_winner("rock", "scissors"))         # Output: Player wins
print(determine_winner("paper", "rock"))            # Output: Player wins
print(determine_winner("scissors", "paper"))        # Output: Player wins

print(determine_winner("rock", "rock"))             # Output: Draw

print(determine_winner("scissors", "rock"))         # Output: Computer wins

# -----------------------------------------------------------------------
# B. Test Invalid Input
# -----------------------------------------------------------------------

choices = ["rock", "paper", "scissors"]

player = input("Your choice: ").strip().lower()

if player not in choices:
    print("Invalid choice!")
else:
    print("Valid choice!")

# -----------------------------------------------------------------------
# C. Test using assertions
# -----------------------------------------------------------------------

assert determine_winner("rock", "scissors") == "Player wins"

assert determine_winner("paper", "rock") == "Player wins"

assert determine_winner("scissors", "paper") == "Player wins"

assert determine_winner("rock", "rock") == "Draw"

assert determine_winner("rock", "paper") == "Computer wins"

print("All tests passed!")

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------