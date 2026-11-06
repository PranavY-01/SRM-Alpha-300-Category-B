# DSA Daily Gym | November | Week 1 | Day 6 | Problem: 266. Palindrome Permutation
# --------------------------------------------------------------------------------------
# Given a string s, return true if a permutation of the string could form a palindrome.
# Constraints:
# 1 <= s.length <= 5000
# s consists of only lowercase English letters.
# --------------------------------------------------------------------------------------

def canPermutePalindrome(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    return odd_count <= 1

if __name__ == "__main__":
    # test cases
    s1 = "code"
    print(canPermutePalindrome(s1))  # Output: False

    s2 = "aab"
    print(canPermutePalindrome(s2))  # Output: True

    s3 = "carerac"
    print(canPermutePalindrome(s3))  # Output: True