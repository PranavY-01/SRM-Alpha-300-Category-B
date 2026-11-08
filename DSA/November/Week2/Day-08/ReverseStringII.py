# DSA Daily Gym | November | Week 2 | Day 8 | Problem: 541. Reverse String II
# --------------------------------------------------------------------------------------
# Given a string s and an integer k, reverse the first k characters for every 2 k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them. If there are less than 2 k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.
# Constraints:
# 1 <= s.length <= 10^4
# s consists of only lowercase English letters.
# 1 <= k <= 10^4
# --------------------------------------------------------------------------------------

def reverseStr(s, k):
    s = list(s)  # Convert string to list for mutability
    n = len(s)

    for i in range(0, n, 2 * k):
        # Reverse the first k characters in the current segment
        left = i
        right = min(i + k - 1, n - 1)  # Ensure we don't go out of bounds

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return ''.join(s)  # Convert list back to string

if __name__ == "__main__":
    # test cases
    s1 = "abcdefg"
    k1 = 2
    print(reverseStr(s1, k1))  # Output: "bacdfeg"

    s2 = "abcd"
    k2 = 2
    print(reverseStr(s2, k2))  # Output: "bacd"

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the string s
# Space Complexity: O(n), due to the conversion of string to list
# Pattern: String Manipulation
# --------------------------------------------------------------------------------------