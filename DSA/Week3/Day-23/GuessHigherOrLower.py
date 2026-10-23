# Week 3 - Day 23 - Problem: 374. Guess Number Higher or Lower
# ----------------------------------------------------------------------------------------
# We are playing a guessing game. A number is picked from 1 to n.
# Every time you guess incorrectly, the API tells you whether the picked
# number is higher or lower than your guess.
# Use the predefined guess(num) API to return the picked number.
#
# API return values:
# -1: Your guess is higher than the picked number.
#  1: Your guess is lower than the picked number.
#  0: Your guess is correct.
#
# Constraints:
# 1 <= n <= 2^31 - 1
# 1 <= pick <= n
# ----------------------------------------------------------------------------------------

def guessNumber(n):
    left = 1
    right = n

    while left <= right:
        mid = left + (right - left) // 2
        result = guess(mid)

        if result == 0:
            return mid
        elif result == -1:
            right = mid - 1
        else:
            left = mid + 1

pick = 6   # Mock value for testing purposes. In the actual problem, the value is pre-defined in the Leetcode.

def guess(num):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


if __name__ == "__main__":
    # Test cases
    n1 = 10
    pick = 6
    print(guessNumber(n1))  # Output: 6

    n2 = 1
    pick = 1
    print(guessNumber(n2))  # Output: 1

    n3 = 2
    pick = 1
    print(guessNumber(n3))  # Output: 1

# -----------------------------------------------------------------------------------------
# Time complexity: O(log n), as the search range is halved in each iteration.
# Space complexity: O(1), as only a few variables are used.
# Pattern: Binary Search on Answer
# How it works: Search the possible numbers from 1 to n.
# If guess(mid) returns 0, the correct number is found.
# If it returns -1, the guess was too high, so search the lower half.
# If it returns 1, the guess was too low, so search the upper half.
# Continue until the picked number is found.
# -----------------------------------------------------------------------------------------
