# DSA Daily Gym | November | Week 2 | Day 13 | Problem: 290. Word Pattern
# --------------------------------------------------------------------------------------
# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
# Constraints:
# 1 <= pattern.length <= 300
# s contains lowercase English letters and spaces.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
# --------------------------------------------------------------------------------------


def wordPattern(pattern, s):
    words = s.split()

    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for i in range(len(pattern)):
        ch = pattern[i]
        word = words[i]

        if ch in char_to_word:
            if char_to_word[ch] != word:
                return False
        else:
            char_to_word[ch] = word

        if word in word_to_char:
            if word_to_char[word] != ch:
                return False
        else:
            word_to_char[word] = ch

    return True

if __name__ == "__main__":
    # test cases
    pattern1 = "abba"
    s1 = "dog cat cat dog"
    print(wordPattern(pattern1, s1))  # Output: True

    pattern2 = "abba"
    s2 = "dog cat cat fish"
    print(wordPattern(pattern2, s2))  # Output: False

    pattern3 = "aaaa"
    s3 = "dog cat cat dog"
    print(wordPattern(pattern3, s3))  # Output: False