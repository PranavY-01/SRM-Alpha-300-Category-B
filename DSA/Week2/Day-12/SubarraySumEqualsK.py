# Week-2 Day-12: 560. Subarray Sum Equals K
# ----------------------------------------------------------------------------------------
# Given an array of integers nums and an integer k, 
# return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
#
# Constraints:
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107
#
# ----------------------------------------------------------------------------------------

from py_compile import main

def subarraySum(nums, k):
    count = 0
    sum = 0
    d = dict()
    d[0] = 1  # Initialize with prefix sum 0 having one occurrence

    for i in range(len(nums)):
        sum += nums[i]
        if (sum - k) in d:
            count += d[sum - k]
        d[sum] = d.get(sum, 0) + 1

    return count

if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(subarraySum(nums, k))  # Output: 2

    nums = [1, 2, 3]
    k = 3
    print(subarraySum(nums, k))  # Output: 2

# ----------------------------------------------------------------------------------------
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Prefix Sum with Hash Map
# How it works: We maintain a running sum and use a hash map to store the frequency of prefix sums.
# For each element, we check if (current_sum - k) exists in the hash map, which indicates that there is a subarray that sums to k.
# We increment the count by the frequency of (current_sum - k) and update the hash map with the current sum.
#----------------------------------------------------------------------------------------
