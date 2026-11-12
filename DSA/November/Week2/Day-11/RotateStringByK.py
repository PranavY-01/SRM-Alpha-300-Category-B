# DSA Daily Gym | November | Week 2 | Day 11 | Problem: Rotate String By K
# --------------------------------------------------------------------------------------
# Given a string s and an integer k, return the string after rotating it to the right by k steps.
# Constraints:
# 1 <= s.length <= 100
# s consists of lowercase English letters.
# 0 <= k <= 100
# --------------------------------------------------------------------------------------

def rotateByK(s, k):
    n = len(s)

    if n == 0 or k == 0:
        return s

    k = k % n
    return s[n-k:] + s[:n-k]

if __name__ == "__main__":
    # test cases
    s1 = "abcdef"
    k1 = 2
    print(rotateByK(s1, k1))  # Output: "efabcd"

    s2 = "HelloWorld"
    k2 = 3
    print(rotateByK(s2, k2))  # Output: "ldHelloWor"

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(n) for the new string created after rotation.
# Pattern: String Rotation
# --------------------------------------------------------------------------------------