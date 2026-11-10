# DSA Daily Gym | November | Week 2 | Day 10 | Problem: 821. Shortest Distance to a Character
# --------------------------------------------------------------------------------------
# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
# Constraints:
# 1 <= s.length <= 10^4
# s consists of lowercase English letters.
# c is a lowercase English letter, and it is guaranteed that c occurs at least once in s.
# --------------------------------------------------------------------------------------

def shortestToChar(s, c):
    n = len(s)
    answer = [0] * n
    prev = -float('inf')

    for i in range(n):
        if s[i] == c:
            prev = i
        answer[i] = i - prev

    prev = float('inf')

    for i in range(n - 1, -1, -1):
        if s[i] == c:
            prev = i
        answer[i] = min(answer[i], prev - i)

    return answer

if __name__ == "__main__":
    # test cases
    s1 = "loveleetcode"
    c1 = "e"
    print(shortestToChar(s1, c1))  # Output: [3,2,1,0,1,0,0,1,2,2,1,0]

    s2 = "aaab"
    c2 = "b"
    print(shortestToChar(s2, c2))  # Output: [3,2,1,0]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the input string s.
# Space Complexity: O(n)
# Pattern: Two Passes - Forward and Backward
# --------------------------------------------------------------------------------------