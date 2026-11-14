# Python For Beginners | Chapter 1: Rock, Paper, Scissors | Class 7. Else and Elif Statements 
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Basic if with elif and else statements
# -----------------------------------------------------------------------

score = 75

if score >= 90:
    print("Excellent")

elif score >= 70:
    print("Good")

else:
    print("Keep practising")

# -----------------------------------------------------------------------
# B. For Rock Paper Scissors Game
# -----------------------------------------------------------------------

player = "rock"
computer = "scissors"

if player == computer:
    print("Draw")

elif player == "rock" and computer == "scissors":
    print("Player wins")

elif player == "paper" and computer == "rock":
    print("Player wins")

elif player == "scissors" and computer == "paper":
    print("Player wins")

else:
    print("Computer wins")

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
