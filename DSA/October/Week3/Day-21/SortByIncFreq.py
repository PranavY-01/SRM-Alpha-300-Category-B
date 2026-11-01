# Week 3 - Day 21 - Problem: 1636. Sort Array by Increasing Frequency
# ----------------------------------------------------------------------------------------
# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
# Return the sorted array.
# Constraints:
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100
# ----------------------------------------------------------------------------------------

def sortByFrequency(nums):
    # Count the frequency of each number
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    n = len(nums)  # Sort the array based on frequency and value

    for i in range(n):
        best = i

        for j in range(i + 1, n):
            if freq[nums[j]] < freq[nums[best]]:   # Lower frequency comes first
                best = j
            elif (freq[nums[j]] == freq[nums[best]]  # If frequencies tie, larger value comes first
                  and nums[j] > nums[best]):
                best = j

        nums[i], nums[best] = nums[best], nums[i]

    return nums

if __name__ == "__main__":
    # Test cases
    nums1 = [1, 1, 2, 2, 2, 3]
    print(sortByFrequency(nums1))  # Output: [3, 1, 1, 2, 2, 2]

    nums2 = [2, 3, 1, 3, 2]
    print(sortByFrequency(nums2))  # Output: [1, 3, 3, 2, 2]

    nums3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    print(sortByFrequency(nums3))  # Output: [5, -1, -6, -6, 4, 4, 1, 1, 1]

# -----------------------------------------------------------------------------------------
# Time complexity: O(n^2) where n is the number of elements in the input array. The outer loop runs n times, and for each iteration, the inner loop may run up to n times in the worst case.
# Space complexity: O(n) for the frequency dictionary that stores the count of each unique number
# Pattern: Frequency Counting and Custom Sorting
# How it works: This implementation first counts the frequency of each number in the input array using a dictionary. 
# Then, it sorts the array in-place based on the frequency of the numbers, with ties broken by the value of the numbers. 
# The sorting is done using a selection sort-like approach, where for each position in the array, we find the best candidate to place there based on the frequency and value criteria.
# -----------------------------------------------------------------------------------------