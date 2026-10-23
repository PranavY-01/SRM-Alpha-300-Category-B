# Week 4 - Day 23 - Problem: 367. Valid Perfect Square
# ----------------------------------------------------------------------------------------
# Given a positive integer num, return True if num is a perfect square.
# Otherwise, return False.
# You must not use any built-in square-root function, such as sqrt().
#
# Constraints:
# 1 <= num <= 2^31 - 1
# ----------------------------------------------------------------------------------------

def isPerfectSquare(num):
    left = 1
    right = num

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1

    return False


if __name__ == "__main__":
    # Test cases
    num1 = 16
    print(isPerfectSquare(num1))  # Output: True

    num2 = 14
    print(isPerfectSquare(num2))  # Output: False

    num3 = 1
    print(isPerfectSquare(num3))  # Output: True

    num4 = 2
    print(isPerfectSquare(num4))  # Output: False

# ----------------------------------------------------------------------------------------
# Time complexity: O(log num), as the search range is halved in every iteration.
# Space complexity: O(1), as only a few variables are used.
# Pattern: Binary Search on Answer
#
# How it works:
# Search for an integer whose square equals num.
# If mid * mid == num, the number is a perfect square.
# If mid * mid < num, search the upper half because mid is too small.
# If mid * mid > num, search the lower half because mid is too large.
# If the search finishes without finding an exact square, return False.
# ----------------------------------------------------------------------------------------
