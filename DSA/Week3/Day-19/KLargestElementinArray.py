# Week 3 - Day 19 - Problem: 215. Kth Largest Element in an Array
# ----------------------------------------------------------------------------------------
# Given an integer array nums and an integer k, return the kth largest element in the array
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.
# Constraints:
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# ----------------------------------------------------------------------------------------

def kLargestElement(nums, k):
    def partition(left, right, pivot_index):
        pivot_value = nums[pivot_index]
        # Move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left

        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # Move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    def quickselect(left, right, k_smallest):
        if left == right:  # If the list contains only one element
            return nums[left]

        pivot_index = (left + right) // 2
        pivot_index = partition(left, right, pivot_index)

        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        else:
            return quickselect(pivot_index + 1, right, k_smallest)

    # kth largest is (len(nums) - k)th smallest
    return quickselect(0, len(nums) - 1, len(nums) - k)

if __name__ == "__main__":
    # Test cases
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print(kLargestElement(nums1, k1))  # Output: 5

    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    print(kLargestElement(nums2, k2))  # Output: 4

# -----------------------------------------------------------------------------------------
# Time complexity: O(n) on average, O(n^2) in the worst case 
# Space complexity: O(1) as we are using constant space for the partitioning process
# Pattern: Quickselect Algorithm
# How it works: This implementation uses the Quickselect algorithm, which is a selection algorithm to find the kth largest element in an unordered list. 
# It works by partitioning the array around a pivot and recursively narrowing down the search space until the kth element is found.
# -----------------------------------------------------------------------------------------