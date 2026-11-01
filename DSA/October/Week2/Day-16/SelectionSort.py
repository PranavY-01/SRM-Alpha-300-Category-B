# Week 2 - Day 16 - 912. Sort an Array (Selection Sort)
# ----------------------------------------------------------------------------------------
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
# 
# Constraints:
# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104
# ----------------------------------------------------------------------------------------

def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        min = i  # Assume the current index is the minimum

        for j in range(i + 1, n):
            if arr[j] < arr[min]:  # Find the index of the minimum element
                min = j

        arr[i], arr[min] = arr[min], arr[i]

    return arr

if __name__ == "__main__":
    # Test cases
    m1 = [64, 25, 12, 22, 11]
    print(selectionSort(m1))  # Output: [11, 12, 22, 25, 64]

    m2 = [5, 3, 8, 6, 2]
    print(selectionSort(m2))  # Output: [2, 3, 5, 6, 8]

    m3 = [1, 2, 3, 5, 7, 6]
    print(selectionSort(m3))  # Output: [1, 2, 3, 5, 6, 7] (half sorted array)

# ----------------------------------------------------------------------------------------
# Time complexity: O(n^2)
# Space complexity: O(1)
# Pattern: Selection Sort
# How it works: The algorithm divides the input list into two parts: 
# a sorted sublist of items which is built up from left to right at the front (left) of the list 
# and a sublist of the remaining unsorted items that occupy the rest of the list. 
# Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. 
# The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, 
# exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.
#----------------------------------------------------------------------------------------