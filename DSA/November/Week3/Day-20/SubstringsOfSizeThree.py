# DSA Daily Gym | November | Week 3 | Day 20 | Problem: 1876. Substrings of Size Three with Distinct Characters
# ----------------------------------------------------------------------------------------
# A string is good if there are no repeated characters.
# Given a string s, return the number of good substrings of length three in s.
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
# A substring is a contiguous sequence of characters in a string.
# Constraints:
# 1 <= s.length <= 100
# s consists of lowercase English letters.
# ----------------------------------------------------------------------------------------

def countGoodSubstrings(s):
    count = 0
    for i in range(len(s) - 2):
        substring = s[i:i + 3]
        if len(set(substring)) == 3:
            count += 1
    return count

if __name__ == "__main__":
    # Test cases
    s = "xyzzaz"
    print(countGoodSubstrings(s))  # Output: 1

    s = "aababcabc"
    print(countGoodSubstrings(s))  # Output: 4

# ------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(1) (since we are only using a fixed-size set for checking distinct characters)
# Pattern: Sliding Window
# ------------------------------------------------------------------------