# Week 12 - Day 13: Permutation in String
# ----------------------------------------------------------------------------------------
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Constraints:
# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.
# ----------------------------------------------------------------------------------------

def checkInclusion(s1, s2):
    if len(s1) > len(s2):   # check if s1 is longer than s2, if so return False
        return False

    s1_count = {}
    s2_count = {}

    for ch in s1:
        s1_count[ch] = s1_count.get(ch, 0) + 1

    for i in range(len(s1) - 1):
        ch = s2[i]
        s2_count[ch] = s2_count.get(ch, 0) + 1

    for i in range(len(s1) - 1, len(s2)):
        ch = s2[i]
        s2_count[ch] = s2_count.get(ch, 0) + 1

        if s2_count == s1_count:
            return True

        left_char = s2[i - len(s1) + 1]
        s2_count[left_char] -= 1

        if s2_count[left_char] == 0:
            del s2_count[left_char]

    return False

if __name__ == "__main__":
    # Test cases
    s1 = "ab"
    s2 = "eidbaooo"
    print(checkInclusion(s1, s2))  # Output: True

    s1 = "ab"
    s2 = "eidboaoo"
    print(checkInclusion(s1, s2))  # Output: False

# ----------------------------------------------------------------------------------------
# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Sliding Window with Hash Map
# How it works: We use a sliding window of size equal to the length of s1 and maintain a frequency count of characters in the current window of s2.
# We compare this frequency count with the frequency count of s1. If they match, it means we have found a permutation of s1 in s2, and we return True.
# We then slide the window by one character to the right, updating the frequency count accordingly, and repeat the process until we have checked all possible windows in s2. If no permutation is found, we return False.
#----------------------------------------------------------------------------------------