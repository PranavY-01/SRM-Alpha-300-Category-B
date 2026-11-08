# DSA Daily Gym | November | Week 1 | Day 7 | Problem: 434. Number of Segments in a String
# --------------------------------------------------------------------------------------
# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.
# Constraints:
# 0 <= s.length <= 300
# s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()-+".
# The string s does not contain any leading or trailing spaces.
# --------------------------------------------------------------------------------------

def countSegments(s):
    if not s:
        return 0

    count = 0
    for i in range(len(s)):
        if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
            count += 1

    return count

if __name__ == "__main__":
    # test cases
    print(countSegments("Hello, my name is John"))  # Output: 5
    print(countSegments("Hello"))     # Output: 1


# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the string s
# Space Complexity: O(1)
# Pattern: String Manipulation
# --------------------------------------------------------------------------------------