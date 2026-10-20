# Week 3 - Day 19 - Problem: 912. Sort an Array (via Counting Sort)
# ----------------------------------------------------------------------------------------
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(n log(n)) time complexity and with the smallest space complexity possible.
# Constraints:
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4
# ----------------------------------------------------------------------------------------


def countingSort(nums):
    if not nums:
        return nums

    # Find minimum and maximum manually
    min = nums[0]
    max = nums[0]

    for n in nums:
        if n < min:
            min = n
        if n > max:
            max = n

    # Create the count array
    countRange = max - min + 1
    count = [0] * countRange

    # Count occurrences
    for n in nums:
        count[n - min] += 1

    # Reconstruct the sorted array
    sorted_index = 0

    for i in range(countRange):
        while count[i] > 0:
            nums[sorted_index] = i + min
            sorted_index += 1
            count[i] -= 1

    return nums

if __name__ == "__main__":
    # Test cases
    nums1 = [5, 2, 3, 1]
    print(countingSort(nums1))  # Output: [1, 2, 3, 5]

    nums2 = [5, 1, 1, 2, 0, 0]
    print(countingSort(nums2))  # Output: [0, 0, 1, 1, 2, 5]

# -----------------------------------------------------------------------------------------
# Time complexity: O(n + k) where n is the number of elements in the input array and k is the range of the input values (max - min).
# Space complexity: O(k) for the count array.
# Pattern: Counting Sort
# How it works: This implementation uses the Counting Sort algorithm, which is efficient for sorting integers within a specific range. 
# It counts the occurrences of each integer and then reconstructs the sorted array based on these counts.
# -----------------------------------------------------------------------------------------