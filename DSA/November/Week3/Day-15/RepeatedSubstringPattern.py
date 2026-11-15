# DSA Daily Gym | November | Week 3 | Day 15 | Problem: 459. Repeated Substring Pattern
# --------------------------------------------------------------------------------------
# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
# Constraints:
# 1 <= s.length <= 104
# s consists of lowercase English letters.
# --------------------------------------------------------------------------------------

def repeatedSubstringPattern(s):
    n = len(s)

    for length in range(1, n // 2 + 1):

        if n % length != 0:
            continue

        match = True

        for i in range(length, n):
            if s[i] != s[i % length]:
                match = False
                break

        if match:
            return True

    return False

if __name__ == "__main__":
    print(repeatedSubstringPattern("abab"))  # Output: True
    print(repeatedSubstringPattern("aba"))   # Output: False
    print(repeatedSubstringPattern("abcabcabcabc"))  # Output: True

# --------------------------------------------------------------------------------------
# Time Complexity: O(n^2), where n is the length of the string s.
# Space Complexity: O(1), as we are using a constant amount of extra space.
# Pattern: String Matching Algorithm
# --------------------------------------------------------------------------------------
