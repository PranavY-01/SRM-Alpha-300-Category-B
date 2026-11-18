# DSA Daily Gym | November | Week 3 | Day 18 | Problem: 791. Custom Sort String
# ----------------------------------------------------------------------------------------
# Given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the returned string.
# Return any permutation of s that satisfies this property.
# Constraints:
# 1 <= order.length <= 26
# 1 <= s.length <= 200
# order and s consist of lowercase English letters.
# All the characters of order are unique.
# ----------------------------------------------------------------------------------------

def customSortString(order, s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    order_set = set(order)
    result = []

    # Append characters according to custom order
    for ch in order:
        if ch in freq:
            result.append(ch * freq[ch])
            freq[ch] = 0

    # Append remaining characters
    for ch in s:
        if ch not in order_set and freq[ch] > 0:
            result.append(ch * freq[ch])
            freq[ch] = 0

    return "".join(result)

if __name__ == "__main__":
    # Test cases
    order = "cba"
    s = "abcd"
    print(customSortString(order, s))  # Output: "cbad"

    order = "bcafg"
    s = "abcd"
    print(customSortString(order, s))  # Output: "bcad"

# ------------------------------------------------------------------------
# Time Complexity: O(n + m), where n is the length of s and m is the length of order.
# Space Complexity: O(n + m)
# Pattern: Hashing, Sorting
# ------------------------------------------------------------------------