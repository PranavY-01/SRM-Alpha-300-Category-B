# Python For Beginners | Chapter 1: Rock, Paper, Scissors | Class 11. Complete Project Implementation
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Complete Implementation of Rock Paper Scissors Game
# -----------------------------------------------------------------------


import random


# -----------------------------
# GAME CONFIGURATION
# -----------------------------

choices = ["rock", "paper", "scissors"]

game_rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


# -----------------------------
# PLAYER INPUT
# -----------------------------

def get_player_name():

    name = input("Enter your name: ").strip()

    if not name:
        name = "Player"

    return name


def get_player_choice():

    while True:

        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        choice = input("Your choice: ").strip().lower()

        # Support both numbers and names
        choice_map = {
            "1": "rock",
            "2": "paper",
            "3": "scissors"
        }

        choice = choice_map.get(choice, choice)

        if choice in choices:
            return choice

        print("Invalid choice. Try again.")


# -----------------------------
# COMPUTER SELECTION
# -----------------------------

def get_computer_choice():

    return random.choice(choices)


# -----------------------------
# WINNER DETERMINATION
# -----------------------------

def determine_winner(player, computer):

    if player == computer:
        return "draw"

    if game_rules[player] == computer:
        return "player"

    return "computer"


# -----------------------------
# DISPLAY ROUND RESULT
# -----------------------------

def display_result(name, player, computer, winner):

    print("\n========== ROUND RESULT ==========")

    print(f"{name}: {player}")
    print(f"Computer: {computer}")

    if winner == "draw":
        print("Result: It's a draw!")

    elif winner == "player":
        print(f"Result: {name} wins!")

    else:
        print("Result: Computer wins!")

    print("==================================")


# -----------------------------
# SCOREBOARD
# -----------------------------

def display_scoreboard(player_score, computer_score, draws):

    print("\n========== SCOREBOARD ==========")

    print(f"Player: {player_score}")
    print(f"Computer: {computer_score}")
    print(f"Draws: {draws}")

    print("================================")


# -----------------------------
# MAIN GAME
# -----------------------------

def play_game():

    print("==============================")
    print("   ROCK PAPER SCISSORS")
    print("==============================")

    name = get_player_name()

    player_score = 0
    computer_score = 0
    draws = 0

    while True:

        player = get_player_choice()

        computer = get_computer_choice()

        winner = determine_winner(player, computer)

        display_result(
            name,
            player,
            computer,
            winner
        )

        # Update scoreboard
        if winner == "player":
            player_score += 1

        elif winner == "computer":
            computer_score += 1

        else:
            draws += 1

        display_scoreboard(
            player_score,
            computer_score,
            draws
        )

        # Play again?
        again = input(
            "\nPlay another round? (y/n): "
        ).strip().lower()

        if again != "y":
            break

    print("\n========== FINAL RESULTS ==========")

    print(f"{name}: {player_score}")
    print(f"Computer: {computer_score}")
    print(f"Draws: {draws}")

    if player_score > computer_score:
        print(f"\nCongratulations, {name}!")

    elif computer_score > player_score:
        print("\nComputer wins overall!")

    else:
        print("\nOverall result: Draw!")

    print("Thanks for playing!")


# -----------------------------
# ENTRY POINT
# -----------------------------

if __name__ == "__main__":
    play_game()

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------