# Python For Beginners | Chapter 1: Rock, Paper, Scissors | Class 2: Calling Functions
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Calling functions
# -----------------------------------------------------------------------

def say_hello():
    print("Hello!")

say_hello()

# -----------------------------------------------------------------------
# B. Calling functions multiple times
# -----------------------------------------------------------------------

def display_score():
    print("Player: 0")
    print("Computer: 0")


display_score()
display_score()
display_score()

# -----------------------------------------------------------------------
# C. Function calling another function
# -----------------------------------------------------------------------

def welcome():
    print("Welcome to the game!")


def display_rules():
    print("Rock beats Scissors")
    print("Paper beats Rock")
    print("Scissors beats Paper")


def start_game():

    welcome()
    display_rules()


start_game()

# -----------------------------------------------------------------------
# D. Passing values between functions
# -----------------------------------------------------------------------

def get_choice():
    return "rock"


def display_choice(choice):
    print(f"Your choice is {choice}")


player_choice = get_choice()

display_choice(player_choice)

# -----------------------------------------------------------------------
# E. Practical RPS implementation
# -----------------------------------------------------------------------

def get_player_choice():
    return "rock"


def get_computer_choice():
    return "scissors"


def display_result(player, computer):

    print(f"Player: {player}")
    print(f"Computer: {computer}")


def start_game():

    player = get_player_choice()
    computer = get_computer_choice()

    display_result(player, computer)


start_game()

# -----------------------------------------------------------------------
# Working Example
# -----------------------------------------------------------------------


def get_player_choice():
    return "rock"


def get_computer_choice():
    return "scissors"


def display_result(player, computer):

    print("\n=== ROUND RESULTS ===")
    print(f"Player: {player}")
    print(f"Computer: {computer}")


def start_game():

    print("Welcome to Rock, Paper, Scissors!")

    player = get_player_choice()
    computer = get_computer_choice()

    display_result(player, computer)


if __name__ == "__main__":
    start_game()
  
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------