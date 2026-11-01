
# Week 4 - Day 22 - Problem: 704. Binary Search
# ----------------------------------------------------------------------------------------
# Given an integer array nums sorted in ascending order and an integer target,
# return the index of target if it exists in nums. Otherwise, return -1.
# You must implement an algorithm with O(log n) runtime complexity.
#
# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All integers in nums are unique.
# nums is sorted in ascending order.
# ----------------------------------------------------------------------------------------

def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    # Test cases
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(search(nums1, target1))  # Output: 4

    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(search(nums2, target2))  # Output: -1

# -----------------------------------------------------------------------------------------
# Time complexity: O(log n), where n is the number of elements in the input array.
# Space complexity: O(1), as only a few pointers and variables are used.
# Pattern: Binary Search
# How it works: Initialize two pointers at the beginning and end of the sorted array.
# Compare the middle element with the target. If equal, return its index.
# If the target is larger, search the right half; otherwise, search the left half.
# Repeat until the target is found or the search interval becomes empty.
# -----------------------------------------------------------------------------------------
