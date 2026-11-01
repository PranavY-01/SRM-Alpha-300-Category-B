# Week 4- Day 27 - Problem: 162. Find Peak Element
# ----------------------------------------------------------------------------------------
# A peak element is an element that is strictly greater than its neighbors.
# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞.
# Constraints:
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.
# ----------------------------------------------------------------------------------------

def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[mid + 1]:            # Peak is in the left part including mid
            right = mid
        else:                                    # Peak is in the right part excluding mid
            left = mid + 1

    return left                  

if __name__ == "__main__":
    # Test cases
    nums1 = [1, 2, 3, 1]
    print(findPeakElement(nums1))  # Output: 2

    nums2 = [1, 2, 1, 3, 5, 6, 4]
    print(findPeakElement(nums2))  # Output: 5

# ----------------------------------------------------------------------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Pattern: Binary Search on 1D Array
# How it works: The algorithm uses binary search to find a peak element in the array. It compares the middle element with its right neighbor 
# to determine which part of the array contains a peak and narrows down the search space accordingly. 
# The index of a peak element is returned.
# ----------------------------------------------------------------------------------------
