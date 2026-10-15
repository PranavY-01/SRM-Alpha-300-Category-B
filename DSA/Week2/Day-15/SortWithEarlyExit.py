# Week 2 - Day 15 - 912. Sort an Array (Bubble Sort with Early Exit)
# ----------------------------------------------------------------------------------------
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
#
# Constraints:
# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104
# ----------------------------------------------------------------------------------------

def SortWithEarlyExit(arr):
    n = len(arr)

    for i in range(n):
        swapped = False    # Flag to check if any swapping occurred in this pass
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Mark that a swap occurred
        if not swapped:   # If no swapping occurred, the array is already sorted, so we can exit early - break used.
            break

    return arr


if __name__ == "__main__":
    # Test cases
    nums = [5, 2, 3, 1]
    print(SortWithEarlyExit(nums))  # Output: [1, 2, 3, 5]

    nums = [5, 1, 1, 2, 0, 0]
    print(SortWithEarlyExit(nums))  # Output: [0, 0, 1, 1, 2, 5]

    nums = [1, 2, 3, 4, 5]
    print(SortWithEarlyExit(nums))  # Output: [1, 2, 3, 4, 5] (Optimized case, early exit)