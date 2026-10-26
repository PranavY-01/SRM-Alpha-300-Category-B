# Week 4 - Day 26 - Problem: 33: Search in Rotated Sorted Array
# ----------------------------------------------------------------------------------------
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.
# Constraints:
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is guaranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4 
# ----------------------------------------------------------------------------------------

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Determine which side is sorted
        if nums[left] <= nums[mid]:  # Left side is sorted
            if nums[left] <= target < nums[mid]:  # Target is in the left sorted part
                right = mid - 1
            else:  # Target is in the right part
                left = mid + 1
        else:  # Right side is sorted
            if nums[mid] < target <= nums[right]:  # Target is in the right sorted part
                left = mid + 1
            else:  # Target is in the left part
                right = mid - 1

    return -1  # Target not found

if __name__ == "__main__":
    # Test cases
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    print(search(nums1, target1))  # Output: 4

    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    print(search(nums2, target2))  # Output: -1

    nums3 = [1]
    target3 = 0
    print(search(nums3, target3))  # Output: -1

# ----------------------------------------------------------------------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Pattern: Binary Search on Rotated Sorted Array
# How it works: The algorithm uses binary search to find the target in a rotated sorted array. It checks which side of the array is sorted and narrows down the search space accordingly.
# ----------------------------------------------------------------------------------------
