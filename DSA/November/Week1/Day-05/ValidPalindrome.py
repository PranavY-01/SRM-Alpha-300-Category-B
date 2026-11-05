# DSA Daily Gym | November | Week 1 | Day 4 | Problem: 125. Valid Palindrome
# --------------------------------------------------------------------------------------
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Constraints:
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
# --------------------------------------------------------------------------------------

def isPalindrome(s):

    filtered_chars = [char.lower() for char in s if char.isalnum()]
    
    return filtered_chars == filtered_chars[::-1]

if __name__ == "__main__":
    # test cases
    s1 = "A man, a plan, a canal: Panama"
    print(isPalindrome(s1))  # Output: True

    s2 = "race a car"
    print(isPalindrome(s2))  # Output: False

    s3 = " "
    print(isPalindrome(s3))  # Output: True

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the string s
# Space Complexity: O(n), for the filtered_chars list
# Pattern: Two Pointers / String Manipulation
# --------------------------------------------------------------------------------------