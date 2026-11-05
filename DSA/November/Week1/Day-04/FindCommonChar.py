# DSA Daily Gym | November | Week 1 | Day 4 | Problem: 1002. Find Common Characters
# --------------------------------------------------------------------------------------
# Given an array of strings words made only from lowercase letters, return a list of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.
# --------------------------------------------------------------------------------------

def commonChars(words):
    common = {}

    # Frequency of first word
    for ch in words[0]:
        common[ch] = common.get(ch, 0) + 1

    # Compare with remaining words
    for word in words[1:]:
        current = {}

        for ch in word:
            current[ch] = current.get(ch, 0) + 1

        # Keep minimum frequency
        for ch in common:
            if ch in current:
                common[ch] = min(common[ch], current[ch])
            else:
                common[ch] = 0

    result = []

    for ch in common:
        for _ in range(common[ch]):
            result.append(ch)

    return result

if __name__ == "__main__":
    # test cases
    words1 = ["bella", "label", "roller"]
    print(commonChars(words1))  # Output: ["e", "l", "l"]

    words2 = ["cool", "lock", "cook"]
    print(commonChars(words2))  # Output: ["c", "o"]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n * k), n = no. of strings, k = average length of strings
# Space Complexity: O(1)
# Pattern: Hash Map - Character Counting
# --------------------------------------------------------------------------------------