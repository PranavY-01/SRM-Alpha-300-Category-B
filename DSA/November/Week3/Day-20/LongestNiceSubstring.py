# DSA Daily Gym | November | Week 3 | Day 20 | Problem: 1763. Longest Nice Substring
# ----------------------------------------------------------------------------------------
# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.
# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.
# Constraints:
# 1 <= s.length <= 100
# s consists of uppercase and lowercase English letters.
# ----------------------------------------------------------------------------------------


def longestNiceSubstring(s):

    def solve(start, end):
        if end - start < 2:
            return ""

        present = set()

        for i in range(start, end):
            present.add(s[i])

        for i in range(start, end):
            ch = s[i]

            if ch.islower():
                opposite = ch.upper()
            else:
                opposite = ch.lower()

            if opposite not in present:
                left_result = solve(start, i)
                right_result = solve(i + 1, end)

                if len(left_result) >= len(right_result):
                    return left_result
                else:
                    return right_result

        return s[start:end]

    return solve(0, len(s))

if __name__ == "__main__":
    # Test cases
    s = "YazaAay"
    print(longestNiceSubstring(s))  # Output: "aAa"

    s = "Bb"
    print(longestNiceSubstring(s))  # Output: "Bb"

    s = "c"
    print(longestNiceSubstring(s))  # Output: ""

# ------------------------------------------------------------------------
# Time Complexity: O(n^2), where n is the length of the string s.
# Space Complexity: O(n), due to the recursion stack.
# Pattern: Divide and Conquer - Character Set Checking
# ------------------------------------------------------------------------