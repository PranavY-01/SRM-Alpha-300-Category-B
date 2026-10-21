# Week 3 - Day 21 - Problem: 75. Sort Colors (Dutch Flag Problem - 3 way partitioning)
# ----------------------------------------------------------------------------------------
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the colors red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
# ----------------------------------------------------------------------------------------


def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

if __name__ == "__main__":
    # Test cases
    nums1 = [2, 0, 2, 1, 1, 0]
    print(sortColors(nums1))  # Output: [0, 0, 1, 1, 2, 2]

    nums2 = [2, 0, 1]
    print(sortColors(nums2))  # Output: [0, 1, 2]

# -----------------------------------------------------------------------------------------
# This problem has already been solved in Day 20 using the Counting Sort approach. The code above is a same implementation approach of the problem.
# -----------------------------------------------------------------------------------------