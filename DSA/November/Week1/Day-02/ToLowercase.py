# DSA Daily Gym | November | Week 1 | Day 2 | Problem: 709. To Lower Case
# --------------------------------------------------------------------------------------
# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
# Constraints:
# 1 <= s.length <= 100
# s consists of printable ASCII characters.
# --------------------------------------------------------------------------------------

def toLowerCase(s):
    result = ""

    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch

    return result

if __name__ == "__main__":
    # test cases
    s1 = "Hello"
    print(toLowerCase(s1))  # Output: "hello"

    s2 = "LOVELY"
    print(toLowerCase(s2))  # Output: "lovely"

    s3 = "Python3.8"
    print(toLowerCase(s3))  # Output: "python3.8"

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the string s
# Space Complexity: O(n), for the result string
# Pattern: String Traversal - Character Case Conversion
# --------------------------------------------------------------------------------------