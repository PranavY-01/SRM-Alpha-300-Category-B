# DSA Daily Gym | November | Week 3 | Day 20 | Problem: 476. Minimum Window Substring
# ----------------------------------------------------------------------------------------
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The test cases will be generated such that the answer is unique.
# Constraints:
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
# ----------------------------------------------------------------------------------------

def minWindow(s, t):
    if len(t) > len(s) or len(t) == 0:
        return ""

    required = {}

    for ch in t:
        required[ch] = required.get(ch, 0) + 1

    window = {}

    required_count = len(required)
    matched = 0

    left = 0
    min_length = float("inf")
    start = 0

    for right in range(len(s)):
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1

        if ch in required:
            if window[ch] == required[ch]:
                matched += 1

        while matched == required_count:
            current_length = right - left + 1

            if current_length < min_length:
                min_length = current_length
                start = left

            left_ch = s[left]

            if left_ch in required:
                if window[left_ch] == required[left_ch]:
                    matched -= 1

            window[left_ch] -= 1
            left += 1

    if min_length == float("inf"):
        return ""

    return s[start:start + min_length]

if __name__ == "__main__":
    # Test cases
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s, t))  # Output: "BANC"

    s = "a"
    t = "a"
    print(minWindow(s, t))  # Output: "a"

    s = "a"
    t = "aa"
    print(minWindow(s, t))  # Output: ""

# ------------------------------------------------------------------------
# Time Complexity: O(m + n), where m is the length of s and n is the length of t.
# Space Complexity: O(m + n), for the required and window dictionaries.
# Pattern: Sliding Window
# ------------------------------------------------------------------------