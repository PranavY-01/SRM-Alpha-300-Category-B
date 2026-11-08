# DSA Daily Gym | November | Week 1 | Day 7 | Problem: 3813. Vowel Consonant Score
# --------------------------------------------------------------------------------------
# Given a string s consisting of lowercase English letters, return the sum of the scores of all prefixes of s.
# Let v be the number of vowels in s and c be the number of consonants in s.
# The score of a prefix is defined as follows:
# If c > 0, the score = floor(v / c) where floor denotes rounding down to the nearest integer.
# Otherwise, the score = 0.
# Return an integer denoting the score of the string.
# Constraints:
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
# --------------------------------------------------------------------------------------

def vowelConsonantScore(s):
    vowels = "aeiou"

    vowel_count = 0
    consonant_count = 0

    for ch in s:

        if 'a' <= ch <= 'z':
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    if consonant_count == 0:
        return 0

    return vowel_count // consonant_count

if __name__ == "__main__":
    # test cases
    s1 = "cooear"
    print(vowelConsonantScore(s1))  # Output: 2

    s2 = "axeyizou"
    print(vowelConsonantScore(s2))  # Output: 1

    s3 = "au 123"
    print(vowelConsonantScore(s3))  # Output: 0
