# Week 4 - Day 26 - Problem: Find Rotation Count in Sorted Array
# ----------------------------------------------------------------------------------------
# Given a sorted array that has been rotated at some unknown pivot, the task is to find the number of times the array has been rotated.
# The number of rotations is equal to the index of the minimum element in the rotated sorted array
# Constraints:
# The array is sorted in ascending order and contains distinct elements.
# ----------------------------------------------------------------------------------------

def findRotationCount(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] > arr[right]:  # Minimum is in the right part
            left = mid + 1
        else:  # Minimum is in the left part including mid
            right = mid

    return left  # The index of the minimum element is the number of rotations

if __name__ == "__main__":
    # Test cases
    arr1 = [15, 18, 2, 3, 6, 12]
    print(findRotationCount(arr1))  # Output: 2

    arr2 = [7, 9, 11, 12, 5]
    print(findRotationCount(arr2))  # Output: 4

    arr3 = [1, 2, 3, 4, 5]
    print(findRotationCount(arr3))  # Output: 0

# ----------------------------------------------------------------------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Pattern: Binary Search on Rotated Sorted Array
# How it works: The algorithm uses binary search to find the index of the minimum element in a rotated sorted array.
# It checks the middle element against the rightmost element to determine which part of the array contains the minimum value and narrows down the search space accordingly. The index of the minimum element corresponds to the number of rotations.
# ----------------------------------------------------------------------------------------