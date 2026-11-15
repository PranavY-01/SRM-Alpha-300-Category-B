# DSA Daily Gym | November | Week 3 | Day 15 | Problem: 796. Rotate String (via substring matching)
# --------------------------------------------------------------------------------------
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position .
# For example, if s = "abcde", then it will be "bcdea" after one shift.
# Constraints:
# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.
# --------------------------------------------------------------------------------------

def containsSubstring(text, pattern, start, end):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return True

    for i in range(start, end):
        if i + m > n:
            break

        j = 0

        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            return True

    return False


def rotateString(s, goal):
    n = len(s)

    if n != len(goal):
        return False

    doubled = s + s

    return containsSubstring(doubled, goal, 0, n)

if __name__ == "__main__":
    print(rotateString("abcde", "cdeab"))  # True
    print(rotateString("abcde", "abced"))  # False

# --------------------------------------------------------------------------------------
# Time Complexity: O(n^2), where n is the length of the string s.
# Space Complexity: O(n), as we are creating a new string of length 2n.
# Pattern: String Matching Algorithm.
# --------------------------------------------------------------------------------------