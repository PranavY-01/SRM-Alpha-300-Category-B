# Week 4 - Day 25 - Problem: 162. Find Peak Element
# ----------------------------------------------------------------------------------------
# A peak element is an element that is strictly greater than its neighbors.
# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞.
# You must write an algorithm that runs in O(log n) time.
# Constraints:
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.
# ----------------------------------------------------------------------------------------

def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1  # Move to the right half
        else:
            right = mid  # Move to the left half

    return left  # return the index of the peak element. return right would also work since left == right at the end of the loop.

if __name__ == "__main__":
    # Test cases
    nums1 = [1, 2, 3, 1]
    print(findPeakElement(nums1))  # Output: 2 (index of peak element 3)

    nums2 = [1, 2, 1, 3, 5, 6, 4]
    print(findPeakElement(nums2))  # Output: 5 (index of peak element 6)

# ----------------------------------------------------------------------------------------
# Time complexity: O(log n), as the search range is halved in every iteration.
# Space complexity: O(1), as only a few variables are used.
# Pattern: Binary Search on Answer
# How it works: The algorithm uses a binary search approach to find a peak element. It compares the middle element with its right neighbor. 
# If the middle element is less than its right neighbor, it means there is a peak in the right half of the array, 
# so we move the left pointer to mid + 1. Otherwise, we move the right pointer to mid, as there could be a peak in the left half or at mid itself. 
# The process continues until left and right converge, at which point we have found a peak element.
# ----------------------------------------------------------------------------------------
