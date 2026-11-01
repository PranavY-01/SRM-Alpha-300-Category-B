# Week 2 - Day 14: 1004. Max Consecutive Ones III
# ----------------------------------------------------------------------------------------
#
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's 
# in the array if you can flip at most k 0's.
#
# Constraints:
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length
# ----------------------------------------------------------------------------------------

def longestOnes(nums, k):
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] == 0:
            k -= 1
        j += 1
        if k < 0:
            if nums[i] == 0:
                k += 1
            i += 1
    return j - i

if __name__ == "__main__":
    # Test cases
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    print(longestOnes(nums, k))  # Output: 6

    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0]
    k = 3
    print(longestOnes(nums, k))  # Output: 10

# ----------------------------------------------------------------------------------------
# Time complexity: O(n)
# Space complexity: O(1)
# Pattern: Sliding Window
# How it works: We use a sliding window approach to keep track of the number of 0's in the current window. 
# We expand the window by moving the right pointer (j) and decrement k when we encounter a 0. 
# If k becomes negative, we shrink the window from the left (i) until k is non-negative again. 
# The maximum length of the window is calculated as j - i, which gives us the maximum number of consecutive 1's after flipping at most k 0's.
#----------------------------------------------------------------------------------------