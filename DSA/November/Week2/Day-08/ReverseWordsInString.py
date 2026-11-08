# DSA Daily Gym | November | Week 2 | Day 8 | Problem: 151. Reverse Words in a String
# --------------------------------------------------------------------------------------
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
# Constraints:
# 1 <= s.length <= 10^4
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
# --------------------------------------------------------------------------------------

def reverseWords(s):
    # Split the string into words, removing extra spaces
    words = []
    i = 0
    n = len(s)

    # Extract words manually
    while i < n:

        # Skip spaces
        while i < n and s[i] == ' ':
            i += 1

        if i >= n:
            break

        word = ""

        # Collect characters of a word
        while i < n and s[i] != ' ':
            word += s[i]
            i += 1

        words.append(word)

    # Reverse word order manually
    left = 0
    right = len(words) - 1

    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1

    return " ".join(words)

if __name__ == "__main__":
    # test cases
    s1 = "the sky is blue"
    print(reverseWords(s1))  # Output: "blue is sky the"

    s2 = "  hello world  "
    print(reverseWords(s2))  # Output: "world hello"

    s3 = "a good   example"
    print(reverseWords(s3))  # Output: "example good a"

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the string s
# Space Complexity: O(n), for the list of words
# Pattern: String Manipulation - Word Reversal
# --------------------------------------------------------------------------------------
