# Python For Beginners | Chapter 1: Rock, Paper, Scissors | Class 6. Function Arguments
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Arguments in Functions
# -----------------------------------------------------------------------

def display_choice(choice):
    print(f"You selected {choice}")


display_choice("rock")

# -----------------------------------------------------------------------
# B. Multiple Arguments in Functions
# -----------------------------------------------------------------------

def display_choices(player, computer):

    print(f"Player: {player}")
    print(f"Computer: {computer}")


display_choices("rock", "scissors")

# -----------------------------------------------------------------------
# C. Returning values
# -----------------------------------------------------------------------

def get_winner(player, computer):

    if player == computer:
        return "Draw"

    return "Game completed"


result = get_winner("rock", "rock")

print(result)

# -----------------------------------------------------------------------
# D. Default Arguments
# -----------------------------------------------------------------------

def display_score(player_score=0, computer_score=0):

    print(f"Player: {player_score}")
    print(f"Computer: {computer_score}")


display_score()
display_score(2, 1)


# -----------------------------------------------------------------------
# E. Keyword Arguments
# -----------------------------------------------------------------------

display_score(
    computer_score=3,
    player_score=5
)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------