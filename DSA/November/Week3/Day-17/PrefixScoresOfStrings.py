# DSA Daily Gym | November | Week 3 | Day 17 | Problem: 2416. Sum of Prefix Scores of Strings
# ----------------------------------------------------------------------------------------
# You are given an array words of size n consisting of non-empty strings.
# The prefix score of a string word is equal to the number of strings in words that have word as a prefix.
# Return an array answer of size n where answer[i] is the sum of prefix scores of all the prefixes of words[i].
# A prefix of a string s is any leading contiguous substring of s.
# Constraints:
# 1 <= n <= 1000
# 1 <= words[i].length <= 1000
# words[i] consists of lowercase English letters.
# ----------------------------------------------------------------------------------------

def sumPrefixScores(words):
    prefix_count = {}
    result = []

    # Count the occurrences of each prefix
    for word in words:
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            prefix_count[prefix] = prefix_count.get(prefix, 0) + 1

    # Calculate the sum of prefix scores for each word
    for word in words:
        score_sum = 0
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            score_sum += prefix_count[prefix]
        result.append(score_sum)

    return result

if __name__ == "__main__":
    # Test cases
    words = ["abc", "ab", "bc", "b"]
    print(sumPrefixScores(words))  # Output: [5, 4, 3, 2]

    words = ["a", "a"]
    print(sumPrefixScores(words))  # Output: [2, 2]

# ----------------------------------------------------------------------------------------
# Time complexity: O(n * m^2), where n is the number of words and m is the average length of the words.
# Space complexity: O(n * m), for storing the prefix counts in the dictionary.
# Pattern: Prefix Counting
# ----------------------------------------------------------------------------------------