# Python For Beginners | Chapter 1: Rock, Paper, Scissors | Class 8. Refactoring and Nested If Statements
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Direct Accessing Dictionary Values
# -----------------------------------------------------------------------

game_rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

print(game_rules["rock"])           # Outputs: scissors

# -----------------------------------------------------------------------
# B. Using the get() method to access dictionary values
# -----------------------------------------------------------------------

print(game_rules.get("rock"))       # Outputs: scissors
print(game_rules.get("lizard"))     # Outputs: None

# -----------------------------------------------------------------------
# C. Default value with the get() method
# -----------------------------------------------------------------------

print(game_rules.get("lizard", "Invalid choice"))

print(game_rules.keys())            # Outputs: dict_keys(['rock', 'paper', 'scissors'])
print(game_rules.values())          # Outputs: dict_values(['scissors', 'rock', 'paper'])
print(game_rules.items())           # Outputs: dict_items([('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')])

# -----------------------------------------------------------------------
# D Iterating through dictionary keys and values
# -----------------------------------------------------------------------

for choice, defeats in game_rules.items():
    print(f"{choice} defeats {defeats}")

for choice in game_rules.keys():
    print(f"Choice: {choice}")

# -----------------------------------------------------------------------
# E. Dictionary-based winner determination
# -----------------------------------------------------------------------

def determine_winner(player, computer):

    if player == computer:
        return "Draw"

    defeated_choice = game_rules.get(player)

    if defeated_choice == computer:
        return "Player wins"

    return "Computer wins"

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------