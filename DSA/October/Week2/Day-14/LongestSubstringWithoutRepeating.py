# Week 2 - Day 14: 3. Longest Substring Without Repeating Characters
# ----------------------------------------------------------------------------------------
# Given a string s, find the length of the longest substring without duplicate characters.
# Constraints:
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# ----------------------------------------------------------------------------------------

def lengthOfLongestSubstring(s):
    left = 0
    seen = {}
    output = 0

    for right, curr in enumerate(s):
        if curr in seen:
            left = max(left, seen[curr] + 1)

        output = max(output, right - left + 1)
        seen[curr] = right

    return output

if __name__ == "__main__":
    # Test cases
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))  # Output: 3

    s = "bbbbb"
    print(lengthOfLongestSubstring(s))  # Output: 1

    s = "pwwkew"
    print(lengthOfLongestSubstring(s))  # Output: 3

# ----------------------------------------------------------------------------------------
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Sliding Window with Hash Map
# How it works: We use a sliding window approach to keep track of the characters in the current substring. We maintain a dictionary to store the last seen index of each character. If we encounter a character that is already in the dictionary and its index is greater than or equal to the left pointer, we move the left pointer to the right of the last seen index of that character. We then update the output with the maximum length of the current substring without repeating characters. Finally, we update the last seen index of the current character in the dictionary.
#----------------------------------------------------------------------------------------