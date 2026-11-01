# Week 4 - Day 26 - Problem: 153: Find Minimum in Rotated Sorted Array
# ----------------------------------------------------------------------------------------
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.
# Constraints:
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.
# ----------------------------------------------------------------------------------------

def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:  # Minimum is in the right part
            left = mid + 1
        else:  # Minimum is in the left part including mid
            right = mid

    return nums[left]  # The minimum element is at index 'left'

if __name__ == "__main__":
    # Test cases
    nums1 = [3, 4, 5, 1, 2]
    print(findMin(nums1))  # Output: 1

    nums2 = [4, 5, 6, 7, 0, 1, 2]
    print(findMin(nums2))  # Output: 0

    nums3 = [11, 13, 15, 17]
    print(findMin(nums3))  # Output: 11

# ----------------------------------------------------------------------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Pattern: Binary Search on Rotated Sorted Array
# How it works: The algorithm uses binary search to find the minimum element in a rotated sorted array. 
# It checks the middle element against the rightmost element to determine which part of the array contains the minimum value and narrows down the search space accordingly.
# ----------------------------------------------------------------------------------------
