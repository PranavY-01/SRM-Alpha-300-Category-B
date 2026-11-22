# DSA Daily Gym | November | Week 3 | Day 21 | Problem: 859. Buddy Strings
# ----------------------------------------------------------------------------------------
# Given two strings s and goal, return true if you can swap two letters in s so that the result is equal to goal, otherwise, return false.
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
# Constraints:
# 1 <= s.length, goal.length <= 2 * 10^4
# s and goal consist of lowercase letters.
# ----------------------------------------------------------------------------------------

def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False

    if s == goal:
        seen = set()

        for ch in s:
            if ch in seen:
                return True

            seen.add(ch)

        return False

    mismatch = []

    for i in range(len(s)):
        if s[i] != goal[i]:
            mismatch.append(i)

            if len(mismatch) > 2:
                return False

    if len(mismatch) != 2:
        return False

    i = mismatch[0]
    j = mismatch[1]

    return s[i] == goal[j] and s[j] == goal[i]

if __name__ == "__main__":
    # Test cases
    s = "ab"
    goal = "ba"
    print(buddyStrings(s, goal))  # Output: True

    s = "ab"
    goal = "ab"
    print(buddyStrings(s, goal))  # Output: False

    s = "aa"
    goal = "aa"
    print(buddyStrings(s, goal))  # Output: True

# ------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the strings s and goal.
# Space Complexity: O(1), as we are using a constant amount of extra space.
# Pattern: String Comparison and Mismatch Tracking
# ------------------------------------------------------------------------