# Week 2 - Day 17 - Problem: 75. Sort Colors (Sort with 3 Elements | Dutch National Flag Problem)
# ----------------------------------------------------------------------------------------
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the colors red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
# ----------------------------------------------------------------------------------------

def sort3elements(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums

if __name__ == "__main__":
    # Test cases
    nums1 = [2, 0, 2, 1, 1, 0]
    print(sort3elements(nums1))  # Output: [0, 0, 1, 1, 2, 2]

    nums2 = [2, 0, 1]
    print(sort3elements(nums2))  # Output: [0, 1, 2]

# -----------------------------------------------------------------------------------------
# Time complexity: O(n^2) 
# Space complexity: O(1) as we are sorting the array in place without using any additional data structures.
# Pattern: Insertion Sort
# How it works: This implementation showcases the insertion sort algorithm to sort an array with 3 elements. Basic insertion sort.
# -----------------------------------------------------------------------------------------
