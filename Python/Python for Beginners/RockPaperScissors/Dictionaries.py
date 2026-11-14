# Python For Beginners | Chapter 1: Rock, Paper, Scissors | Class 3: Dictionaries
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Creating a dictionary
# -----------------------------------------------------------------------

game_rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

print(game_rules)

# -----------------------------------------------------------------------
# B. Accessing values in a dictionary
# -----------------------------------------------------------------------

print(game_rules)

# -----------------------------------------------------------------------
# C. Checking whether a key exists
# -----------------------------------------------------------------------

if "rock" in game_rules:
    print("Rock exists!")

player = "rock"
computer = "scissors"

if game_rules[player] == computer:
    print("Player wins!")

# -----------------------------------------------------------------------
# D. Adding a new key-value pair to a dictionary
# -----------------------------------------------------------------------

game_rules["lizard"] = "paper"
game_rules["lizard"] = "scissors"

print(game_rules)

# -----------------------------------------------------------------------
# E. Removing a key-value pair from a dictionary
# -----------------------------------------------------------------------

del game_rules["lizard"]

print(game_rules)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------