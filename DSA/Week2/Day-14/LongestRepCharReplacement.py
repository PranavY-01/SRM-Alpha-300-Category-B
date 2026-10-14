# Week 2 - Day 14: 424. Longest Repeating Character Replacement
# ----------------------------------------------------------------------------------------
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
# Constraints:
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length
# ----------------------------------------------------------------------------------------

def characterReplacement(s, k):
    max_count = 0
    left = 0
    freq = {}
        
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1 # Increment the frequency of the character at the right pointer
        max_count = max(max_count, freq[s[right]]) # Update the max_count to be the maximum frequency of any character in the current window
            
        if right - left + 1 - max_count > k:
            freq[s[left]] -= 1    # Decrement the frequency of the character at the left pointer
            left += 1
                
    return len(s) - left

if __name__ == "__main__":
    # Test cases
    s = "ABAB"
    k = 2
    print(characterReplacement("ABAB", 2))  # Output: 4

    s = "AABABBA"
    k = 1
    print(characterReplacement("AABABBA", 1))  # Output: 4

# ----------------------------------------------------------------------------------------
# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Sliding Window with Hash Map
# How it works: We use a sliding window approach to keep track of the frequency of characters in the current window.
# We maintain a variable max_count to store the count of the most frequent character in the current window. If the length of the current window minus max_count is greater than k, it means we need to shrink the window from the left. We update the frequency count accordingly and continue expanding the window from the right. The maximum length of the valid window is calculated as len(s) - left, which gives us the length of the longest substring containing the same letter after performing at most k operations.
#----------------------------------------------------------------------------------------
