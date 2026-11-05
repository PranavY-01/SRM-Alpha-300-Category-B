# DSA Daily Gym | November | Week 1 | Day 5 | Problem: 9. Palindrome Number
# --------------------------------------------------------------------------------------
# Given an integer x, return true if x is a palindrome, and false otherwise.
# Constraints:
# -2^31 <= x <= 2^31 - 1
# --------------------------------------------------------------------------------------

def isPalindrome(x):
    if x < 0:
        return False

    original = x
    reversed_num = 0

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10

    return original == reversed_num

if __name__ == "__main__":
    # test cases
    x1 = 121
    print(isPalindrome(x1))  # Output: True

    x2 = -121
    print(isPalindrome(x2))  # Output: False

    x3 = 10
    print(isPalindrome(x3))  # Output: False

# --------------------------------------------------------------------------------------
# Time Complexity: O(log(n))
# Space Complexity: O(1)
# Pattern: Mathematical Manipulation 
# --------------------------------------------------------------------------------------