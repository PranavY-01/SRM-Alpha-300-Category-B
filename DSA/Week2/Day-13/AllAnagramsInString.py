# Week 12 | Day 13: 438. Find All Anagrams in a String
# ----------------------------------------------------------------------------------------
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Constraints:
# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.
# ----------------------------------------------------------------------------------------
def findAnagrams(s, p):
    if len(p) > len(s):
        return []

    p_count = {}
    s_count = {}
    result = []

    for ch in p:
        p_count[ch] = p_count.get(ch, 0) + 1     # Count characters in p

    for i in range(len(p) - 1):
        ch = s[i]                                # Initialize the first window
        s_count[ch] = s_count.get(ch, 0) + 1 

    for i in range(len(p) - 1, len(s)):
        ch = s[i]
        s_count[ch] = s_count.get(ch, 0) + 1

        if s_count == p_count:                          # Compare character frequencies
            result.append(i - len(p) + 1)

        left_char = s[i - len(p) + 1]
        s_count[left_char] -= 1                       # Remove outgoing character

        if s_count[left_char] == 0:
            del s_count[left_char]

    return result

if __name__ == "__main__":
    # Test cases
    s = "cbaebabacd"
    p = "abc"
    print(findAnagrams(s, p))  # Output: [0, 6]

    s = "abab"
    p = "ab"
    print(findAnagrams(s, p))  # Output: [0, 1, 2]

# ----------------------------------------------------------------------------------------
# Time complexity: O(n)
# Space complexity: O(1) 
# Pattern: Sliding Window with Hash Map
# How it works: We use a sliding window of size equal to the length of p and maintain a frequency count of characters in the current window of s.
# We compare this frequency count with the frequency count of p. If they match, it means we have found an anagram, and we record the starting index of the window.
# We then slide the window by one character to the right, updating the frequency count accordingly, and repeat the process until we have checked all possible windows in s.
#----------------------------------------------------------------------------------------