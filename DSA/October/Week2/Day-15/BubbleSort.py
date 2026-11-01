# Week 2 - Day 15 - 912. Sort an Array (Bubble Sort)
# ----------------------------------------------------------------------------------------
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
#
# Constraints:
# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104
# ----------------------------------------------------------------------------------------

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1): 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]   
    return arr


if __name__ == "__main__":
    # Test cases
    nums = [5, 2, 3, 1]
    print(bubble_sort(nums))  # Output: [1, 2, 3, 5]

    nums = [5, 1, 1, 2, 0, 0]
    print(bubble_sort(nums))  # Output: [0, 0, 1, 1, 2, 5]

# ----------------------------------------------------------------------------------------
# Time complexity: O(n^2)
# Space complexity: O(1)
# Pattern: Bubble Sort
# How it works: We iterate through the array multiple times, comparing adjacent elements and swapping them if they are in the wrong order. This process continues until the entire array is sorted. The largest unsorted element "bubbles" to its correct position in each iteration.
#----------------------------------------------------------------------------------------