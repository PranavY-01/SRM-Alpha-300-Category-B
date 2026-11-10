# DSA Daily Gym | November | Week 2 | Day 9 | Problem: 557. Reverse Words in a String III
# --------------------------------------------------------------------------------------
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Constraints:
# 1 <= s.length <= 5 * 10^4
# s contains printable ASCII characters.
# --------------------------------------------------------------------------------------

def reverseWords(s):
    chars = list(s)
    start = 0

    for i in range(len(chars) + 1):
        if i == len(chars) or chars[i] == " ":
            left = start
            right = i - 1

            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

            start = i + 1

    return "".join(chars)

if __name__ == "__main__":
    # test cases
    s1 = "Let's take LeetCode contest"
    print(reverseWords(s1))  # Output: "s'teL ekat edoCteeL tsetnoc"

    s2 = "Mr Ding"
    print(reverseWords(s2))  # Output: "rM gniD"

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the input string s. 
# Space Complexity: O(n)
# Pattern: Sliding Window - Character Swap
# --------------------------------------------------------------------------------------