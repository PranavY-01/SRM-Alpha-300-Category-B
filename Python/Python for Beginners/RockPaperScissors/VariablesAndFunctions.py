# Rock, Paper, Scissors
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Functions
# -----------------------------------------------------------------------

def welcome():
    print("Welcome to Rock, Paper, Scissors!")


welcome()

# -----------------------------------------------------------------------
# B. Variables outside functions
# -----------------------------------------------------------------------

player = "rock"
computer = "paper"

print(player)
print(computer)

# -----------------------------------------------------------------------
# C. Variables inside functions
# -----------------------------------------------------------------------


def display_choices():

    rock = "rock"
    paper = "paper"
    scissors = "scissors"

    print(rock)
    print(paper)
    print(scissors)


display_choices()

# -----------------------------------------------------------------------
# D. Functions with parameters
# -----------------------------------------------------------------------

def display_choice(choice):

    print(f"You selected {choice}")


display_choice("rock")
display_choice("paper")
display_choice("scissors")

# -----------------------------------------------------------------------
# E. Combining variables and functions
# -----------------------------------------------------------------------

player = "rock"
computer = "scissors"


def display_choices():

    print(f"Player chose: {player}")
    print(f"Computer chose: {computer}")


display_choices()

# -----------------------------------------------------------------------
# F. Chapter Exercise
# -----------------------------------------------------------------------


player = "paper"
computer = "rock"

def show_game():
    print("=== GAME STATUS ===")
    print(f"Player: {player}")
    print(f"Computer: {computer}")

show_game()

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
