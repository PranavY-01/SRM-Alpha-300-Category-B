# Week 4 - Day 25 - Problem: 1095: Find in Mountain Array
# ----------------------------------------------------------------------------------------
# You may recall that an array arr is a mountain array if and only if:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr and an integer target, return the index i such that arr[i] == target.
# If there are multiple such indices, return the smallest one.
# If there is no such index, return -1.
# You must solve it in O(log(arr.length)) time complexity.
# Constraints:
# 3 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^6
# arr is guaranteed to be a mountain array.
# 0 <= target <= 10^6
# ----------------------------------------------------------------------------------------

# Step 1: Find the peak index of the mountain array using binary search.
# Step 2: Perform binary search on the ascending part of the mountain array (from the start to the peak) to find the target.
# Step 3: If the target is not found in the ascending part, perform binary search on the descending part of the mountain array (from the peak to the end) to find the target.
def findInMountainArray(target, mountain_arr):
    def find_peak_index(arr):   
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

    def binary_search(arr, target, left, right, ascending=True):   # search in ascending or descending order based on the 'ascending' flag
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if ascending:  # search in ascending order
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if arr[mid] > target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    peak_index = find_peak_index(mountain_arr)  # Find the peak index of the mountain array
    index = binary_search(mountain_arr, target, 0, peak_index)
    if index != -1:  
        return index
    return binary_search(mountain_arr, target, peak_index + 1, len(mountain_arr) - 1, ascending=False)  # Search in the descending part of the mountain array if not found in the ascending part

if __name__ == "__main__":
    # Test cases
    mountain_arr1 = [1, 2, 3, 4, 5, 3, 1]
    target1 = 3
    print(findInMountainArray(target1, mountain_arr1))  # Output: 2

    mountain_arr2 = [0, 1, 2, 4, 2, 1]
    target2 = 3
    print(findInMountainArray(target2, mountain_arr2))  # Output: -1

    mountain_arr3 = [0, 5, 3, 1]
    target3 = 1
    print(findInMountainArray(target3, mountain_arr3))  # Output: 3

# ----------------------------------------------------------------------------------------
# Time complexity: O(log n), as the search range is halved in every iteration for both peak finding and binary search.
# Space complexity: O(1).
# Pattern: Binary Search on Answer
# How it works: The algorithm first finds the peak index of the mountain array using binary search. Then, it performs two binary searches: one on the ascending part of the array (from the start to the peak) and another on the descending part (from the peak to the end). If the target is found in either part, its index is returned; otherwise, -1 is returned.
# ----------------------------------------------------------------------------------------