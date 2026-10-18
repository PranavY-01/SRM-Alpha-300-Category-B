# Week 3 - Day 18 - Problem: 88. Merge Sorted Array
# ----------------------------------------------------------------------------------------
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# Constraints:
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# -10^9 <= nums1[i], nums2[j] <= 10^9
# ----------------------------------------------------------------------------------------

def merge_sorted_array(nums1, m, nums2, n):
    # Start from the end of both arrays and merge them in reverse order
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1

    # If there are remaining elements in nums2, copy them over to nums1
    while n > 0:
        nums1[n - 1] = nums2[n - 1]
        n -= 1

if __name__ == "__main__":
    # Test cases
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge_sorted_array(nums1, m, nums2, n)
    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge_sorted_array(nums1, m, nums2, n)
    print(nums1)  # Output: [1]

# -----------------------------------------------------------------------------------------
# Time complexity: O(m + n) where m and n are the lengths of nums1 and nums2 respectively.
# Space complexity: O(1) as we are merging the arrays in place without using any additional data structures.
# Pattern: Two Pointer Technique
# How it works: This implementation merges two sorted arrays in place by starting from the end of both arrays and filling nums1 from the back. 
# It compares the last elements of both arrays and places the larger one at the end of nums1, moving backwards until all elements are merged.
# -----------------------------------------------------------------------------------------
