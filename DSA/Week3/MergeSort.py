# Week 3 - Day 18 - Problem: 912. Sort an Array (via Merge Sort)
# ----------------------------------------------------------------------------------------
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(n log(n)) time complexity and with the smallest space complexity possible.
# Constraints:
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4
# ----------------------------------------------------------------------------------------

def merge(left, right):   # Merges two sorted lists into a single sorted list
    res = []
    left_i, right_i = 0, 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            res.append(left[left_i])             # Append the smaller element from the left half to the result list
            left_i += 1
        else:
            res.append(right[right_i])
            right_i += 1

    # Append any remaining elements from the left or right half
    res.extend(left[left_i:])
    res.extend(right[right_i:])

    return res

def merge_sort(nums):   # Main Function: merge sort
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])

    return merge(left_half, right_half)    # Calls the merge function to combine the sorted halves

if __name__ == "__main__":
    # Test cases
    nums1 = [5, 2, 3, 1]
    print(merge_sort(nums1))  # Output: [1, 2, 3, 5]

    nums2 = [5, 1, 1, 2, 0, 0]
    print(merge_sort(nums2))  # Output: [0, 0, 1, 1, 2, 5]

# -----------------------------------------------------------------------------------------
# Time complexity: O(n log n)
# Space complexity: O(n) as we are using additional space for the merged list.
# Pattern: Divide and Conquer Approach
# How it works: This implementation showcases the merge sort algorithm to sort an array of integers. It recursively divides the array into halves, sorts each half, and then merges the sorted halves back together.
# -----------------------------------------------------------------------------------------
