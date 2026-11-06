# DSA Daily Gym | November | Week 1 | Day 6 | Problem: 409. Longest Palindrome
# --------------------------------------------------------------------------------------
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.
# --------------------------------------------------------------------------------------

def longestPalindrome(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    length = 0
    odd_found = False

    for count in char_count.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_found = True

    if odd_found:
        length += 1

    return length

if __name__ == "__main__":
    # test cases
    s1 = "abccccdd"
    print(longestPalindrome(s1))  # Output: 7

    s2 = "a"
    print(longestPalindrome(s2))  # Output: 1

    s3 = "Aa"
    print(longestPalindrome(s3))  # Output: 1

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the string s
# Space Complexity: O(1)
# Pattern: Counting Characters
# --------------------------------------------------------------------------------------