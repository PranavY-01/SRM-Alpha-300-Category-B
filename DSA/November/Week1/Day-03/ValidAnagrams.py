# DSA Daily Gym | November | Week 1 | Day 2 | Problem: 242. Valid Anagram
# --------------------------------------------------------------------------------------
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# --------------------------------------------------------------------------------------

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for ch in t:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1

    return True

if __name__ == "__main__":
    # test cases
    s1 = "anagram"
    t1 = "nagaram"
    print(isAnagram(s1, t1))  # Output: True

    s2 = "rat"
    t2 = "car"
    print(isAnagram(s2, t2))  # Output: False

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the strings s and t
# Space Complexity: O(1), since the count dictionary will have at most 26 entries for lowercase English letters
# Pattern: Hash Map - Character Counting
# --------------------------------------------------------------------------------------