# DSA Daily Gym | November | Week 1 | Day 4 | Problem: 383. Ransom Note
# --------------------------------------------------------------------------------------
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# Constraints:
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
# --------------------------------------------------------------------------------------

def canConstruct(ransomNote, magazine):
    count = {}

    # Count magazine characters
    for ch in magazine:
        count[ch] = count.get(ch, 0) + 1

    # Consume characters for ransom note
    for ch in ransomNote:
        if ch not in count or count[ch] == 0:
            return False

        count[ch] -= 1

    return True

if __name__ == "__main__":
    # test cases
    ransomNote1 = "a"
    magazine1 = "b"
    print(canConstruct(ransomNote1, magazine1))  # Output: False

    ransomNote2 = "aa"
    magazine2 = "ab"
    print(canConstruct(ransomNote2, magazine2))  # Output: False

    ransomNote3 = "aa"
    magazine3 = "aab"
    print(canConstruct(ransomNote3, magazine3))  # Output: True

# --------------------------------------------------------------------------------------
# Time Complexity: O(n + m), where n is the length of ransomNote and m is the length of magazine
# Space Complexity: O(1)
# Pattern: Hash Map - Character Counting
# --------------------------------------------------------------------------------------