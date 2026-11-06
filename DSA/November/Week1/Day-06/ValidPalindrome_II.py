# DSA Daily Gym | November | Week 1 | Day 5 | Problem: 680. Valid Palindrome II
# --------------------------------------------------------------------------------------
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
# Constraints:
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# --------------------------------------------------------------------------------------

def validPalindrome(s):

    def is_palindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return (
                is_palindrome(left + 1, right) or
                is_palindrome(left, right - 1)
            )

        left += 1
        right -= 1

    return True

if __name__ == "__main__":
    # test cases
    s1 = "abca"
    print(validPalindrome(s1))  # Output: True

    s2 = "racecar"
    print(validPalindrome(s2))  # Output: True

    s3 = "abcdefg"
    print(validPalindrome(s3))  # Output: False

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the string s
# Space Complexity: O(1)
# Pattern: Two Pointers - Palindrome Check
# --------------------------------------------------------------------------------------