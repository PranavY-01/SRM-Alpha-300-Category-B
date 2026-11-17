# DSA Daily Gym | November | Week 3 | Day 17 | Problem: 2062. Count Vowel Substrings of a String
# ----------------------------------------------------------------------------------------
# A substring is a contiguous (non-empty) sequence of characters within a string.
# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.
# Given a string word, return the number of vowel substrings in word.  
# Constraints:
# 1 <= word.length <= 100
# word consists of lowercase English letters.
# ----------------------------------------------------------------------------------------

def countVowelSubstrings(word):
    vowels = set('aeiou')
    count = 0

    for i in range(len(word)):
        if word[i] not in vowels:
            continue
        
        seen_vowels = set()
        for j in range(i, len(word)):
            if word[j] not in vowels:
                break
            seen_vowels.add(word[j])
            if len(seen_vowels) == 5:
                count += 1

    return count

if __name__ == "__main__":
    # Test cases
    word = "aeiouu"
    print(countVowelSubstrings(word))  # Output: 2

    word = "unicornarihan"
    print(countVowelSubstrings(word))  # Output: 0

    word = "cuaieuouac"
    print(countVowelSubstrings(word))  # Output: 7

# ----------------------------------------------------------------------------------------
# Time complexity: O(n^2)
# Space complexity: O(1)
# Pattern: Nested Loops
# ----------------------------------------------------------------------------------------