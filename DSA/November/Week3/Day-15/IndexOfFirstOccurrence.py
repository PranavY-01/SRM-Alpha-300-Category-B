# DSA Daily Gym | November | Week 3 | Day 15 | Problem: 28. Find the Index of the First Occurrence in a String
# --------------------------------------------------------------------------------------
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Constraints:
# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.
# --------------------------------------------------------------------------------------

def strStr(haystack, needle):
    if not needle:
        return 0  
    
    haystack_length = len(haystack)
    needle_length = len(needle)

    for i in range(haystack_length - needle_length + 1):
        if haystack[i:i + needle_length] == needle:
            return i  

    return -1  # If needle not found

if __name__ == "__main__":

    print(strStr("sadbutsad", "sad"))  # Output: 0
    print(strStr("leetcode", "leeto"))  # Output: -1

# --------------------------------------------------------------------------------------
# Time Complexity: O((N - M) * M), where N is the length of haystack and M is the length of needle. 
# Space Complexity: O(1), as we are using a constant amount of extra space.
# Pattern: String Matching Algorithm
# --------------------------------------------------------------------------------------
