# Week 3 - Day 20 - Problem: 75. Sort Colors (Dutch Flag Problem - Counting Style)
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
    # Count occurrences of each color
    count = [0, 0, 0]  # count[0] for red (0), count[1] for white (1), count[2] for blue (2)

    for num in nums:
        count[num] += 1

    # Reconstruct the sorted array based on counts
    index = 0
    for color in range(3):
        for _ in range(count[color]):
            nums[index] = color
            index += 1

    return nums

if __name__ == "__main__":
    # Test cases
    nums1 = [2, 0, 2, 1, 1, 0]
    print(sortColors(nums1))  # Output: [0, 0, 1, 1, 2, 2]

    nums2 = [2, 0, 1]
    print(sortColors(nums2))  # Output: [0, 1, 2]

# -----------------------------------------------------------------------------------------
# Time complexity: O(n) where n is the number of elements in the input array.
# Space complexity: O(1) as we are using a fixed-size count array of size 3.
# Pattern: Counting Sort
# -----------------------------------------------------------------------------------------