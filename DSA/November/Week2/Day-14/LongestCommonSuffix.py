# DSA Daily Gym | November | Week 2 | Day 14 | Problem: Longest Common Suffix
# --------------------------------------------------------------------------------------
# Write a function to find the longest common suffix string amongst an array of strings.
# If there is no common suffix, return an empty string "".
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.
# --------------------------------------------------------------------------------------

def longestCommonSuffix(strs):
    if not strs:
        return ""

    suffix = strs[0]

    for i in range(1, len(strs)):
        while not strs[i].endswith(suffix):
            suffix = suffix[1:]
            if not suffix:
                return ""

    return suffix

if __name__ == "__main__":
    # test cases
    strs1 = ["flower", "power", "tower"]
    print(longestCommonSuffix(strs1))  # Output: "ower"

    strs2 = ["dog", "racecar", "car"]
    print(longestCommonSuffix(strs2))  # Output: ""

# --------------------------------------------------------------------------------------
# Time Complexity: O(n * m), where n is the number of strings and m is the length of the shortest string.
# Space Complexity: O(1) 
# Pattern: Horizontal scanning
# --------------------------------------------------------------------------------------
