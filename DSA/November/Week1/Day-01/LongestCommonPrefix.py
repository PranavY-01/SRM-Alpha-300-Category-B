# DSA Daily Gym | November | Week 1 | Day 1 | Problem: 14. Longest Common Prefix
# --------------------------------------------------------------------------------------
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.
# --------------------------------------------------------------------------------------

def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = ""

    for i in range(len(strs[0])):
        char = strs[0][i]

        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return prefix

        prefix += char

    return prefix

if __name__ == "__main__":
    # test cases
    strs1 = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strs1))  # Output: "fl"

    strs2 = ["dog", "racecar", "car"]
    print(longestCommonPrefix(strs2))  # Output: ""

    strs3 = ["interview", "internet", "internal"]
    print(longestCommonPrefix(strs3))  # Output: "inte"

# --------------------------------------------------------------------------------------
# Time Complexity: O(n * m), where n is the number of strings and m is the length of the shortest string
# Space Complexity: O(1)
# Pattern: String Traversal - Vertical Scanning
# --------------------------------------------------------------------------------------