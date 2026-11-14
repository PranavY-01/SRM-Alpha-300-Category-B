# DSA Daily Gym | November | Week 2 | Day 14 | Problem: 14. Longest Common Prefix
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

    prefix = strs[0]

    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

if __name__ == "__main__":
    # test cases
    strs1 = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strs1))  # Output: "fl"

    strs2 = ["dog", "racecar", "car"]
    print(longestCommonPrefix(strs2))  # Output: ""

# --------------------------------------------------------------------------------------
# Time Complexity: O(n * m), where n is the number of strings and m is the length of the shortest string.
# Space Complexity: O(1) since we are using a constant amount of space.
# Pattern: Horizontal scanning
# --------------------------------------------------------------------------------------
