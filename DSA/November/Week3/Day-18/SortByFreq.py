# DSA Daily Gym | November | Week 3 | Day 18 | Problem: 451. Sort Characters By Frequency
# ----------------------------------------------------------------------------------------
# Given a string s, sort it in decreasing order based on the frequency of the characters.
# Return the sorted string. If there are multiple answers, return any of them.
# Constraints:
# 1 <= s.length <= 5 * 10^5
# s consists of uppercase and lowercase English letters and digits.
# ----------------------------------------------------------------------------------------


def mergeSort(chars, freq):
    if len(chars) <= 1:
        return chars

    mid = len(chars) // 2
    left = mergeSort(chars[:mid], freq)
    right = mergeSort(chars[mid:], freq)

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if freq[left[i]] >= freq[right[j]]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def frequencySort(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    chars = mergeSort(list(freq.keys()), freq)

    result = []

    for ch in chars:
        result.append(ch * freq[ch])

    return "".join(result)


if __name__ == "__main__":
    # Test cases
    s = "tree"
    print(frequencySort(s))  # Output: "eert" or "eetr"

    s = "cccaaa"
    print(frequencySort(s))  # Output: "aaaccc" or "cccaaa"

    s = "Aabb"
    print(frequencySort(s))  # Output: "bbAa" or "bbaA"


# ----------------------------------------------------------------------------------------
# Time complexity: O(n log n), where n is the length of the string s.
# Space complexity: O(n), for storing the frequency counts and the result.
# Pattern: Merge Sort
# ----------------------------------------------------------------------------------------