# DSA Daily Gym | November | Week 2 | Day 11 | Problem: 796. Rotate String
# --------------------------------------------------------------------------------------
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.
# Constraints:
# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.
# --------------------------------------------------------------------------------------

def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    return goal in (s + s)

if __name__ == "__main__":
    # test cases
    s1 = "abcde"
    goal1 = "cdeab"
    print(rotateString(s1, goal1))  # Output: True

    s2 = "abcde"
    goal2 = "abced"
    print(rotateString(s2, goal2))  # Output: False

    s3 = "aa"
    goal3 = "aa"
    print(rotateString(s3, goal3))  # Output: True

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(n).
# Pattern: String Manipulation, String Matching
# --------------------------------------------------------------------------------------