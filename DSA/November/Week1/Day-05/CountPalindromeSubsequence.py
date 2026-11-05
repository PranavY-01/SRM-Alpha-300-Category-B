# DSA Daily Gym | November | Week 1 | Day 5 | Problem: 2484. Count Palindromic Subsequences
# --------------------------------------------------------------------------------------
# Given a string of digits s, return the number of palindromic subsequences of s having length 5. 
# Since the answer may be very large, return it modulo 10^9 + 7.
# Note: A string is palindromic if it reads the same forward and backward.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
# Constraints:
# 1 <= s.length <= 10^5
# s consists of digits from '0' to '9'.
# --------------------------------------------------------------------------------------

def countPalindromicSubsequences(s):
    count = 0
    n = len(s)

    def expand(left, right):
        total = 0

        while left >= 0 and right < n and s[left] == s[right]:
            total += 1
            left -= 1
            right += 1

        return total

    for i in range(n):
        # Odd-length palindromes
        count += expand(i, i)

        # Even-length palindromes
        count += expand(i, i + 1)

    return count

if __name__ == "__main__":
    # test cases
    s1 = "12321"
    print(countPalindromicSubsequences(s1))  # Output: 7

    s2 = "11111"
    print(countPalindromicSubsequences(s2))  # Output: 15

    s3 = "1234567890"
    print(countPalindromicSubsequences(s3))  # Output: 10

# --------------------------------------------------------------------------------------
# Time Complexity: O(n^2), where n is the length of the string s
# Space Complexity: O(1)
# Pattern: Expand Around Center
# --------------------------------------------------------------------------------------