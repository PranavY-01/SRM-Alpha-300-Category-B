# Week 3 - Day 24 - Problem: Ceiling Problem using Binary Search Approach
# ----------------------------------------------------------------------------------------
# Given a sorted array of integers and a target value, find the smallest element in the array that is greater than or equal to the target value (the ceiling of the target).
# If such an element does not exist, return -1.
# Constraints:
# 1 <= arr.length <= 10^5
# -10^9 <= arr[i], target <= 10^9
# ----------------------------------------------------------------------------------------

def findCeiling(arr, target):
    left, right = 0, len(arr) - 1
    ceiling_index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return arr[mid]  # Exact match found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            ceiling_index = mid  # Potential ceiling found
            right = mid - 1  # Search in the left half

    return arr[ceiling_index] if ceiling_index != -1 else -1

if __name__ == "__main__":
    # Test cases
    arr1 = [1, 2, 8, 10, 10, 12, 19]
    target1 = 5
    print(findCeiling(arr1, target1))  # Output: 8

    arr2 = [1, 2, 8, 10, 10, 12, 19]
    target2 = 20
    print(findCeiling(arr2, target2))  # Output: -1

    arr3 = [1, 2, 8, 10, 10, 12, 19]
    target3 = 0
    print(findCeiling(arr3, target3))  # Output: 1

# ----------------------------------------------------------------------------------------
# Time complexity: O(log n), as the search range is halved in every iteration.  
# Space complexity: O(1), as only a few variables are used.
# Pattern: Binary Search on Answer
# ----------------------------------------------------------------------------------------
