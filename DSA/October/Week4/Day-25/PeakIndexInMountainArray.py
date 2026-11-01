# Week 4 - Day 25 - Problem: 852. Peak Index in a Mountain Array
# ----------------------------------------------------------------------------------------
# Let's call an array arr a mountain if the following properties hold: arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
# You must solve it in O(log(arr.length)) time complexity.
# Constraints:
# 3 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^6
# arr is guaranteed to be a mountain array.
# ----------------------------------------------------------------------------------------

def peakIndexInMountainArray(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # Move to the right half
        else:
            right = mid  # Move to the left half

    return left  

if __name__ == "__main__":
    # Test cases
    arr1 = [0, 1, 0]
    print(peakIndexInMountainArray(arr1))  # Output: 1

    arr2 = [0, 2, 1, 0]
    print(peakIndexInMountainArray(arr2))  # Output: 1

    arr3 = [0, 10, 5, 2]
    print(peakIndexInMountainArray(arr3))  # Output: 1

# ----------------------------------------------------------------------------------------
# Time complexity: O(log n), as the search range is halved in every iteration.
# Space complexity: O(1), as only a few variables are used.
# Pattern: Binary Search on Answer
# How it works: The algorithm uses a binary search approach to find the peak index in a mountain array. It compares the middle element with its right neighbor.
# If the middle element is less than its right neighbor, it means there is a peak in the right half of the array, so we move the left pointer to mid + 1. Otherwise, we move the right pointer to mid, as there could be a peak in the left half or at mid itself.
# The process continues until left and right converge, at which point we have found the peak index.
# ----------------------------------------------------------------------------------------
