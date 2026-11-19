# DSA Daily Gym | November | Week 3 | Day 19 | Problem: 524. Longest Word in Dictionary through Deleting
# ----------------------------------------------------------------------------------------
# Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given characters of s.
# If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
# Constraints:
# 1 <= s.length <= 1000
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 1000
# s and dictionary[i] consist of lowercase English letters.
# ----------------------------------------------------------------------------------------

def isSubsequence(word, s):
    i = 0
    j = 0

    while i < len(word) and j < len(s):
        if word[i] == s[j]:
            i += 1

        j += 1

    return i == len(word)


def isLexicographicallySmaller(a, b):
    i = 0

    while i < len(a) and i < len(b):
        if a[i] < b[i]:
            return True
        elif a[i] > b[i]:
            return False

        i += 1

    return len(a) < len(b)


def findLongestWord(s, dictionary):
    best = ""

    for word in dictionary:
        if not isSubsequence(word, s):
            continue

        if len(word) > len(best):
            best = word

        elif len(word) == len(best):
            if isLexicographicallySmaller(word, best):
                best = word

    return best

if __name__ == "__main__":
    # Test cases
    s = "abpcplea"
    dictionary = ["ale", "apple", "monkey", "plea"]
    print(findLongestWord(s, dictionary))  # Output: "apple"

    s = "abpcplea"
    dictionary = ["a", "b", "c"]
    print(findLongestWord(s, dictionary))  # Output: "a"

# ------------------------------------------------------------------------
# Time Complexity: O(n * m), where n is the length of s and m is the total length of all words in the dictionary.
# Space Complexity: O(1)
# Pattern: Two Pointers, String Manipulation
# ------------------------------------------------------------------------