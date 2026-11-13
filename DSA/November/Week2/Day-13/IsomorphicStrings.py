# DSA Daily Gym | November | Week 2 | Day 13 | Problem: 205. Isomorphic Strings
# --------------------------------------------------------------------------------------
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.
# Constraints:
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s and t consist of any valid ASCII character.
# --------------------------------------------------------------------------------------

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        a = s[i]
        b = t[i]

        if a in s_to_t:
            if s_to_t[a] != b:
                return False
        else:
            s_to_t[a] = b

        if b in t_to_s:
            if t_to_s[b] != a:
                return False
        else:
            t_to_s[b] = a

    return True

if __name__ == "__main__":
    # test cases
    s1 = "egg"
    t1 = "add"
    print(isIsomorphic(s1, t1))  # Output: True

    s2 = "foo"
    t2 = "bar"
    print(isIsomorphic(s2, t2))  # Output: False

    s3 = "paper"
    t3 = "title"
    print(isIsomorphic(s3, t3))  # Output: True

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the strings s and t.
# Space Complexity: O(n) for the two dictionaries used to store character mappings.
# Pattern: Hash Map
# --------------------------------------------------------------------------------------
