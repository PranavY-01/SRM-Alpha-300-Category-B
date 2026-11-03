# November | Week 1 | Day 3 | Problem: 387. First Unique Character in a String
# --------------------------------------------------------------------------------------
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Constraints:
# 1 <= s.length <= 10^5
# s consists of only lowercase English letters.
# --------------------------------------------------------------------------------------

def firstUniqChar(s):
    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i

    return -1

if __name__ == "__main__":
    # test cases
    s1 = "leetcode"
    print(firstUniqChar(s1))  # Output: 0

    s2 = "loveleetcode"
    print(firstUniqChar(s2))  # Output: 2

    s3 = "aabb"
    print(firstUniqChar(s3))  # Output: -1

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the string s
# Space Complexity: O(1), since the count dictionary will have at most 26 entries for lowercase English letters
# Pattern: Hash Map - Character Counting
# --------------------------------------------------------------------------------------