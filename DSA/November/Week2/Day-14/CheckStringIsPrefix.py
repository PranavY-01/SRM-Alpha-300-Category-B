# DSA Daily Gym | November | Week 2 | Day 14 | Problem: 1961. Check If String Is a Prefix of Array
# --------------------------------------------------------------------------------------
# Given a string s and an array of strings words, determine whether s is a prefix of the concatenation of words.
# A string s is a prefix of a string t if t starts with the same characters as s.
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 10
# 1 <= s.length <= 1000
# words[i] and s consist of lowercase English letters.
# --------------------------------------------------------------------------------------


def isPrefixOfWord(sentence, searchWord):
    words = sentence.split()

    for i in range(len(words)):
        word = words[i]

        if len(searchWord) > len(word):
            continue

        match = True

        for j in range(len(searchWord)):
            if word[j] != searchWord[j]:
                match = False
                break

        if match:
            return i + 1

    return -1

if __name__ == "__main__":
    # test cases
    sentence1 = "i love eating burger"
    searchWord1 = "burg"
    print(isPrefixOfWord(sentence1, searchWord1))  # Output: 4

    sentence2 = "this problem is an easy problem"
    searchWord2 = "pro"
    print(isPrefixOfWord(sentence2, searchWord2))  # Output: 2

    sentence3 = "i am tired"
    searchWord3 = "you"
    print(isPrefixOfWord(sentence3, searchWord3))  # Output: -1

# --------------------------------------------------------------------------------------
# Time Complexity: O(n * m), where n is the number of words in the sentence and m is the length of the searchWord.
# Space Complexity: O(n) for storing the words in the sentence after splitting.
# Pattern: String Matching
# --------------------------------------------------------------------------------------