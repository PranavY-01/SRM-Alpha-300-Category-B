# Week 4 - Day 22 - Problem: 35. Search Insert Position
# ----------------------------------------------------------------------------------------
# Given a sorted array of distinct integers nums and a target value, return the
# index if the target exists. Otherwise, return the index where the target
# should be inserted to maintain ascending order.
# You must implement an algorithm with O(log n) runtime complexity.
#
# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct integers sorted in ascending order.
# -10^4 <= target <= 10^4
# ----------------------------------------------------------------------------------------

def searchInsert(nums, target):
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

    return left


if __name__ == "__main__":
    # Test cases
    nums1 = [1, 3, 5, 6]
    target1 = 5
    print(searchInsert(nums1, target1))  # Output: 2

    nums2 = [1, 3, 5, 6]
    target2 = 2
    print(searchInsert(nums2, target2))  # Output: 1

    nums3 = [1, 3, 5, 6]
    target3 = 7
    print(searchInsert(nums3, target3))  # Output: 4

# -----------------------------------------------------------------------------------------
# Time complexity: O(log n), where n is the number of elements in the input array.
# Space complexity: O(1), as only a few pointers and variables are used.
# Pattern: Binary Search / Lower Bound
# How it works: Use binary search to locate the target in the sorted array.
# If the target exists, return its index. Otherwise, continue adjusting the
# search boundaries until the interval becomes empty.
# At termination, the left pointer represents the correct insertion position.
# -----------------------------------------------------------------------------------------
