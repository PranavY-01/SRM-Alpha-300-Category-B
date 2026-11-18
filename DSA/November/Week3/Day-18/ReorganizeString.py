# DSA Daily Gym | November | Week 3 | Day 18 | Problem: 767. Reorganize String
# ----------------------------------------------------------------------------------------
# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
# Return any possible rearrangement of s or return an empty string if not possible.
# Constraints:
# 1 <= s.length <= 500
# s consists of lowercase English letters.
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


def reorganizeString(s):
    n = len(s)
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    max_freq = 0

    for ch in freq:
        if freq[ch] > max_freq:
            max_freq = freq[ch]

    if max_freq > (n + 1) // 2:
        return ""

    chars = mergeSort(list(freq.keys()), freq)

    result = [""] * n
    index = 0

    for ch in chars:
        count = freq[ch]

        while count > 0:
            if index >= n:
                index = 1

            result[index] = ch
            index += 2
            count -= 1

    return "".join(result)

if __name__ == "__main__":
    # Test cases
    s = "aab"
    print(reorganizeString(s))  # Output: "aba"

    s = "aaab"
    print(reorganizeString(s))  # Output: ""

# ----------------------------------------------------------------------------------------
# Time Complexity: O(n log n) due to sorting the characters based on frequency.
# Space Complexity: O(n) for storing the frequency of characters and the result string.
# Pattern: String Manipulation - Merge Sort
# ----------------------------------------------------------------------------------------