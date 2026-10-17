# Week 2 - Day 17 - Problem:Sort a nearly sorted array (using Insertion Sort)
# ----------------------------------------------------------------------------------------
# Given an array of integers nums, sort the array in ascending order using the insertion sort algorithm.
# You must solve the problem without using any built-in functions 
# in O(nlog(n)) time complexity and with the smallest space complexity possible.
# Constraints:
# 1 <= nums.length <= 5000
# -5000 <= nums[i] <= 5000
# ----------------------------------------------------------------------------------------

def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and key < nums[j]:  # Basic Insertion Sort 
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key   # Insert the key at the correct position in the sorted part of the array

    return nums

if __name__ == "__main__":
    # Test cases
    nums1 = [5, 2, 3, 1]
    print(insertionSort(nums1))  # Output: [1, 2, 3, 5]

    nums2 = [5, 1, 1, 2, 0, 0]
    print(insertionSort(nums2))  # Output: [0, 0, 1, 1, 2, 5]

# -----------------------------------------------------------------------------------------
# Time complexity: O(n^2) in the worst case (when the array is sorted in reverse order.)
# Space complexity: O(1) as we are sorting the array in place without using any additional data structures.
# Pattern: Insertion Sort
# Change: There's no change in the code as its already optimized and met the requirements of both problems. The code still works as expected.
# -----------------------------------------------------------------------------------------