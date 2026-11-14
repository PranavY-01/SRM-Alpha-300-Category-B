# Python For Beginners | Chapter 1: Rock, Paper, Scissors | Class 5. Libraries, Lists and Methods
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Importing libraries
# -----------------------------------------------------------------------

import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

print(computer)

# -----------------------------------------------------------------------
# B. List Methods
# -----------------------------------------------------------------------

choices = ["rock", "paper", "scissors"]

# Add an element
choices.append("lizard")

# Remove an element
choices.remove("lizard")

# Get the number of elements
print(len(choices))

# Check whether an element exists
print("rock" in choices)

# -----------------------------------------------------------------------
# C. Additional List Methods
# -----------------------------------------------------------------------

numbers = [5, 2, 8, 1, 9]

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.append(10)
print(numbers)

numbers.pop()
print(numbers)

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------