# Week 2 - Day 15 - 912. Sort an Array (Sort array by Parity using Bubble Sort)
# ----------------------------------------------------------------------------------------
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
#
# Constraints:
# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104
# ----------------------------------------------------------------------------------------

def sortByParity(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):  
            if arr[j] % 2 == 1 and arr[j + 1] % 2 == 0:   # Parity check: if current is odd and next is even, swap them.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

if __name__ == "__main__":
    # Test cases
    m1 = [3, 1, 2, 4]
    print(sortByParity(m1))  # Output: [2, 4, 3, 1] 

    m2 = [0, 1, 2]
    print(sortByParity(m2))  # Output: [0, 2, 1] 

    m3 = [5, 3, 1]
    print(sortByParity(m3))  # Output: [5, 3, 1] (All odd numbers)

# ----------------------------------------------------------------------------------------
# Time complexity: O(n^2)
# Space complexity: O(1)
# Pattern: Bubble Sort with Parity Check
# How it works: We iterate through the array multiple times, comparing adjacent elements. If the current element is odd and the next element is even, we swap them. This process continues until all even numbers are moved to the front of the array and all odd numbers are moved to the back. The largest unsorted element "bubbles" to its correct position in each iteration.
#----------------------------------------------------------------------------------------