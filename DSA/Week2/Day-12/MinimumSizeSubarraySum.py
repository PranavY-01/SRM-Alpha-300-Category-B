# Week-2 Day-12: 209. Minimum Size Subarray Sum
# ----------------------------------------------------------------------------------------
# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a subarray whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.
#
# Constraints:
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
#
# ----------------------------------------------------------------------------------------

from py_compile import main


def minSubArrayLen(target, nums):
    i = 0
    window_sum = 0
    min_len = float("inf")

    for j in range(len(nums)):
        window_sum += nums[j]              
        while window_sum >= target:       
            min_len = min(min_len, j - i + 1)
            window_sum -= nums[i]
            i += 1

    return 0 if min_len == float("inf") else min_len


if __name__ == "__main__":
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(minSubArrayLen(target, nums)) # Output: 2

    target = 4
    nums = [1, 4, 4]
    print(minSubArrayLen(target, nums))  # Output: 1

    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    print(minSubArrayLen(target, nums))  # Output: 0

# ----------------------------------------------------------------------------------------
# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Sliding Window with Two Pointers
# How it works: We use two pointers, i and j, to maintain a sliding window. 
# We expand the window by moving j and contract it by moving i, 
# always keeping track of the minimum length of a subarray with a sum greater than or equal to the target.
#----------------------------------------------------------------------------------------