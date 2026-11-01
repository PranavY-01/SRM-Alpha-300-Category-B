# Week 3 - Day 19 - Problem: 912. Sort an Array (via Quick Sort 3 way partitioning)
# ----------------------------------------------------------------------------------------
# Given an array of integers nums, sort the array in ascending order using Quick Sort with 3-way partitioning.
# Partition elements into values less than, equal to, and greater than the pivot, sorting in-place without built-in sorting functions.
# Constraints:
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4
# ----------------------------------------------------------------------------------------

def quickSort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]  # Choose the middle element as the pivot
    left = [x for x in nums if x < pivot]  # Elements less than the pivot
    middle = [x for x in nums if x == pivot]  # Elements equal to the pivot
    right = [x for x in nums if x > pivot]  # Elements greater than the pivot

    return quickSort(left) + middle + quickSort(right)  # Recursively sort and combine

if __name__ == "__main__":
    # Test cases
    nums1 = [5, 2, 3, 1]
    print(quickSort(nums1))  # Output: [1, 2, 3, 5]

    nums2 = [5, 1, 1, 2, 0, 0]
    print(quickSort(nums2))  # Output: [0, 0, 1, 1, 2, 5]

# -----------------------------------------------------------------------------------------
# This implementation approach is exact same that of the previous Quick Sort exercise, since its already using left, middle and right partitioning.
# -----------------------------------------------------------------------------------------
