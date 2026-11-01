# Week 3 - Day 20 - Problem: Sort an Array of 0s and 1s (via Counting Style)
# ----------------------------------------------------------------------------------------
# Given an array of integers nums containing only 0s and 1s, sort the array in ascending order in-place without using any built-in sorting functions.
# Constraints:
# 1 <= nums.length <= 10^5
# ----------------------------------------------------------------------------------------

def sort01Array(nums):
    # Count occurrences of 0s and 1s
    count = [0, 0]  # count[0] for 0s, count[1] for 1s

    for num in nums:
        count[num] += 1

    # Reconstruct the sorted array based on counts
    index = 0
    for value in range(2):  # Only two values: 0 and 1
        for _ in range(count[value]):
            nums[index] = value
            index += 1

    return nums

if __name__ == "__main__":
    # Test cases
    nums1 = [1, 0, 1, 0, 1]
    print(sort01Array(nums1))  # Output: [0, 0, 1, 1, 1]

    nums2 = [1, 1, 1, 0, 0]
    print(sort01Array(nums2))  # Output: [0, 0, 0, 1, 1]

    nums3 = [0, 1]
    print(sort01Array(nums3))  # Output: [0, 1] (already sorted)

# -----------------------------------------------------------------------------------------
# Time complexity: O(n) where n is the number of elements in the input array.
# Space complexity: O(1) as we are using a fixed-size count array of size 2.
# Pattern: Counting Sort
# How it works: This implementation uses a counting approach to count the occurrences of 0s and 1s in the input array. 
# It then reconstructs the sorted array based on these counts, ensuring that all 0s come before all 1s.
# -----------------------------------------------------------------------------------------
