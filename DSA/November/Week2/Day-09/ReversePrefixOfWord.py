# DSA Daily Gym | November | Week 2 | Day 9 | Problem: 2000. Reverse Prefix of Word
# --------------------------------------------------------------------------------------
# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive).
# If the character ch does not exist in word, do nothing.   
# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive).
# Return the resulting string. 
# Constraints:
# 1 <= word.length <= 250
# word consists of lowercase English letters.
# ch is a lowercase English letter.
# --------------------------------------------------------------------------------------

def reversePrefix(word, ch):
    chars = list(word)

    end = -1

    for i in range(len(chars)):
        if chars[i] == ch:
            end = i
            break

    if end == -1:
        return word

    left = 0
    right = end

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)

if __name__ == "__main__":
    # test cases
    word1 = "abcdefd"
    ch1 = "d"
    print(reversePrefix(word1, ch1))  # Output: "dcbaefd"

    word2 = "xyxzxe"
    ch2 = "z"
    print(reversePrefix(word2, ch2))  # Output: "zxyxxe"

    word3 = "abcd"
    ch3 = "z"
    print(reversePrefix(word3, ch3))  # Output: "abcd"

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the input string word.
# Space Complexity: O(n)
# Pattern: Reverse String - Two Pointers
# --------------------------------------------------------------------------------------
