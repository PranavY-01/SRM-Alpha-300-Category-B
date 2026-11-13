# DSA Daily Gym | November | Week 2 | Day 13 | Problem: 890. Find and Replace Pattern
# --------------------------------------------------------------------------------------
# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.
# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.
# Constraints:
# 1 <= pattern.length <= 20
# 1 <= words.length <= 50
# words[i].length == pattern.length
# words[i] and pattern are lowercase English letters.
# --------------------------------------------------------------------------------------

def matchesPattern(word, pattern):
    if len(word) != len(pattern):
        return False

    word_to_pattern = {}
    pattern_to_word = {}

    for i in range(len(word)):
        a = word[i]
        b = pattern[i]

        if a in word_to_pattern:
            if word_to_pattern[a] != b:
                return False
        else:
            word_to_pattern[a] = b

        if b in pattern_to_word:
            if pattern_to_word[b] != a:
                return False
        else:
            pattern_to_word[b] = a

    return True


def findAndReplacePattern(words, pattern):
    result = []

    for word in words:
        if matchesPattern(word, pattern):
            result.append(word)

    return result

if __name__ == "__main__":
    # test cases
    words1 = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern1 = "abb"
    print(findAndReplacePattern(words1, pattern1))  # Output: ["mee", "aqq"]

    words2 = ["a", "b", "c"]
    pattern2 = "a"
    print(findAndReplacePattern(words2, pattern2))  # Output: ["a", "b", "c"]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n * m), where n is the number of words and m is the length of the pattern.
# Space Complexity: O(m) for the dictionaries used to store character mappings.
# Pattern: Hash Map
# --------------------------------------------------------------------------------------