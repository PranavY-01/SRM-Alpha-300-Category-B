# DSA Daily Gym | November | Week 1 | Day 8 | Problem: 917. Reverse Only Letters
# --------------------------------------------------------------------------------------
# Given a string s, reverse the string according to the following rules:
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Constraints:
# 1 <= s.length <= 100
# s consists of printable ASCII characters.
# --------------------------------------------------------------------------------------

def reverseOnlyLetters(s):
    chars = list(s)

    left = 0
    right = len(chars) - 1

    while left < right:

        # Skip non-letters from left
        if not (
            'a' <= chars[left] <= 'z' or
            'A' <= chars[left] <= 'Z'
        ):
            left += 1
            continue

        # Skip non-letters from right
        if not (
            'a' <= chars[right] <= 'z' or
            'A' <= chars[right] <= 'Z'
        ):
            right -= 1
            continue

        # Swap letters
        chars[left], chars[right] = chars[right], chars[left]

        left += 1
        right -= 1

    return "".join(chars)

if __name__ == "__main__":
    # test cases
    s1 = "ab-cd"
    print(reverseOnlyLetters(s1))  # Output: "dc-ba"

    s2 = "a-bC-dEf-ghIj"
    print(reverseOnlyLetters(s2))  # Output: "j-Ih-gfE-dCba"

    s3 = "Test1ng-Leet=code-Q!"
    print(reverseOnlyLetters(s3))  # Output: "Qedo1ct-eeLg=ntse-T!"