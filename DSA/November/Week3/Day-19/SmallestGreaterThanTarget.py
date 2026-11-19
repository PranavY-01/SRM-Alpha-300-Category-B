# DSA Daily Gym | November | Week 3 | Day 19 | Problem: 744. Find Smallest Letter Greater Than Target
# ----------------------------------------------------------------------------------------
# Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.
# Note that the letters wrap around. For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
# Constraints:  
# 2 <= letters.length <= 10^4
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# target is a lowercase English letter.
# ----------------------------------------------------------------------------------------

def nextGreatestLetter(letters, target):
    left, right = 0, len(letters) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    return letters[left % len(letters)]

if __name__ == "__main__":
    # Test cases
    letters = ["c", "f", "j"]
    target = "a"
    print(nextGreatestLetter(letters, target))  # Output: "c"

    letters = ["c", "f", "j"]
    target = "c"
    print(nextGreatestLetter(letters, target))  # Output: "f"

    letters = ["x","x","y","y"]
    target = "z"
    print(nextGreatestLetter(letters, target))  # Output: "x"

# ------------------------------------------------------------------------
# Time Complexity: O(log n), where n is the length of letters.
# Space Complexity: O(1)
# Pattern: Binary Search
# ------------------------------------------------------------------------