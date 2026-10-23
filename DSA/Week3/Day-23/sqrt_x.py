# Week 3 - Day 23 - Problem: 69. Sqrt(x)
# ----------------------------------------------------------------------------------------
# Given a non-negative integer x, return the square root of x rounded down
# to the nearest integer. The returned integer should be non-negative.
# You must not use any built-in exponent function or operator.
#
# Constraints:
# 0 <= x <= 2^31 - 1
# ----------------------------------------------------------------------------------------

def mySqrt(x):
    left = 0
    right = x
    answer = 0

    while left <= right:
        mid = left + (right - left) // 2

        if mid * mid <= x:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


if __name__ == "__main__":
    # Test cases
    x1 = 4
    print(mySqrt(x1))  # Output: 2

    x2 = 8
    print(mySqrt(x2))  # Output: 2

    x3 = 0
    print(mySqrt(x3))  # Output: 0

# -----------------------------------------------------------------------------------------
# Time complexity: O(log x), as the search range is halved in every iteration.
# Space complexity: O(1), as only a few variables are used.
# Pattern: Binary Search on Answer
# How it works: Search for the largest integer whose square is less than or equal to x.
# If mid * mid <= x, mid is a valid answer, so store it and search for a larger value.
# Otherwise, mid is too large, so search the lower half.
# When the search ends, answer contains the integer square root rounded down.
# -----------------------------------------------------------------------------------------
