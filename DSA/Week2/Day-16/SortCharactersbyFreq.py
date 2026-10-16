# Week 2 - Day 16 - Problem 451. Sort Characters By Frequency
# ----------------------------------------------------------------------------------------
# Given a string s, sort it in decreasing order based on the frequency of the characters.
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.
#
# Constraints:
# 1 <= s.length <= 5 * 105
# s consists of uppercase and lowercase English letters and digits.
# ----------------------------------------------------------------------------------------

def frequencySort(s):
    # Count the frequency of each character
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    result = []  

    while freq:
        max_char = None
        max_count = 0

        for char in freq:
            if freq[char] > max_count:
                max_char = char
                max_count = freq[char]

        result.append(max_char * max_count)   # Add the character multiplied by its frequency to result

        del freq[max_char]   # Remove the processed character

    return ''.join(result) 

if __name__ == "__main__":
    # Test cases
    s1 = "tree"
    print(frequencySort(s1))  # Output: "eert"

    s2 = "cccaaa"
    print(frequencySort(s2))  # Output: "cccaaa"

    s3 = "Aabb"
    print(frequencySort(s3))  # Output: "bbAa"

# ----------------------------------------------------------------------------------------
# Time complexity: O(n^2) in the worst case due to the nested loop for finding the max frequency character, where n is the length of the string.
# Space complexity: O(n) for storing the frequency of characters in the dictionary.
# Pattern: Frequency Count and Sorting
# How it works: We first count the frequency of each character in the string using a dictionary. Then, we repeatedly find the character with the highest frequency, append it to the result string multiplied by its frequency, and remove it from the frequency dictionary until all characters are processed. Finally, we join the list of characters to form the sorted string based on frequency.
#-----------------------------------------------------------------------------------------