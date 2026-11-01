# DSA Daily Gym | November | Week 1 | Day 1 | Problem: 58. Length of Last Word
# --------------------------------------------------------------------------------------
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# Constraints:
# 1 <= s.length <= 10^4
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.
# --------------------------------------------------------------------------------------

def length_of_last_word(s):
    i = len(s) - 1
    # Step 1: Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1
    # Step 2: Count characters in the last word
    count = 0

    while i >= 0 and s[i] != ' ':
        count += 1
        i -= 1

    return count

if __name__ == "__main__":
    # test cases
    s1 = "Hello World"
    print(length_of_last_word(s1))  # Output: 5

    s2 = "   fly me   to   the moon  "
    print(length_of_last_word(s2))  # Output: 4

    s3 = "luffy is still joyboy"
    print(length_of_last_word(s3))  # Output: 6

# --------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: String Traversal
# --------------------------------------------------------------------------------------