# DSA Daily Gym | November | Week 1 | Day 3 | Problem: 49. Group Anagrams
# --------------------------------------------------------------------------------------
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Constraints:
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# --------------------------------------------------------------------------------------

def groupAnagrams(strs):
    groups = {}
    for word in strs:
        freq = [0] * 26
        for ch in word:
            index = ord(ch) - ord('a')
            freq[index] += 1
        key = tuple(freq)
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())

if __name__ == "__main__":
    # test cases
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs1))  # Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

    strs2 = [""]
    print(groupAnagrams(strs2))  # Output: [[""]]

    strs3 = ["a"]
    print(groupAnagrams(strs3))  # Output: [["a"]]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n * k), n = no. of strings, k = average length of strings
# Space Complexity: O(n * k), for the groups dictionary
# Pattern: Hash Map - Character Grouping
# --------------------------------------------------------------------------------------