# Python For Beginners | Chapter 1: Rock, Paper, Scissors | Class 4: User Input
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Getting user input
# -----------------------------------------------------------------------

player = input("Choose rock, paper or scissors: ")

print(f"You selected {player}")

# -----------------------------------------------------------------------
# B. Validating user input
# -----------------------------------------------------------------------

player = input("Your choice: ").strip().lower()

choices = ["rock", "paper", "scissors"]

player = input("Your choice: ").strip().lower()

if player in choices:
    print("Valid choice!")
else:
    print("Invalid choice!")

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------