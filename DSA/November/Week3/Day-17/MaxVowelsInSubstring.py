# DSA Daily Gym | November | Week 3 | Day 17 | Problem: 1456. Maximum Number of Vowels in a Substring of Given Length
# ----------------------------------------------------------------------------------------
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length
# ----------------------------------------------------------------------------------------

def maxVowels(s, k):
    vowels = set('aeiou')
    max_count = 0
    current_count = 0

    for i in range(len(s)):
        if s[i] in vowels:
            current_count += 1
        
        if i >= k:
            if s[i - k] in vowels:
                current_count -= 1
        
        max_count = max(max_count, current_count)

    return max_count

if __name__ == "__main__":
    # Test cases
    s = "abciiidef"
    k = 3
    print(maxVowels(s, k))  # Output: 3

    s = "aeiou"
    k = 2
    print(maxVowels(s, k))  # Output: 2

    s = "leetcode"
    k = 3
    print(maxVowels(s, k))  # Output: 2

# ----------------------------------------------------------------------------------------
# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Sliding Window
# ----------------------------------------------------------------------------------------