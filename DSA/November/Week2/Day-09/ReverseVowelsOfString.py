# DSA Daily Gym | November | Week 2 | Day 9 | Problem: 345. Reverse Vowels of a String
# --------------------------------------------------------------------------------------
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
# Constraints:
# 1 <= s.length <= 3 * 10^5
# s consist of printable ASCII characters.
# --------------------------------------------------------------------------------------

def reverseVowels(s):
    vowels = set("aeiouAEIOU")
    chars = list(s)
    left, right = 0, len(chars) - 1

    while left < right:
        while left < right and chars[left] not in vowels:
            left += 1
        while left < right and chars[right] not in vowels:
            right -= 1

        if left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return "".join(chars)

if __name__ == "__main__":
    # test cases
    s1 = "hello"
    print(reverseVowels(s1))  # Output: "holle"

    s2 = "leetcode"
    print(reverseVowels(s2))  # Output: "leotcede"

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the input string s.
# Space Complexity: O(n)
# Pattern: Character Swap
# --------------------------------------------------------------------------------------