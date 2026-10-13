# Week 2 - Day 13: Contains Duplicate II
# ----------------------------------------------------------------------------------------
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 104
# ----------------------------------------------------------------------------------------
def containsNearbyDuplicate(nums, k):
    num_dict = {}
    for i, num in enumerate(nums):
        if num in num_dict and i - num_dict[num] <= k:
            return True
        num_dict[num] = i
    return False

if __name__ == "__main__": 
    # Test cases
    nums = [1, 2, 3, 1]
    k = 3
    print(containsNearbyDuplicate(nums, k))  # Output: True

    nums = [1, 0, 1, 1]
    k = 1
    print(containsNearbyDuplicate(nums, k))  # Output: True

    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(containsNearbyDuplicate(nums, k))  # Output: False

# ----------------------------------------------------------------------------------------
# Time complexity: O(n)
# Space complexity: O(n)
# Pattern: Hash Map
# How it works: We use a hash map to store the last index of each number encountered in the array.
# As we iterate through the array, we check if the current number has been seen before and if the difference between the current index and the last index of that number is less than or equal to k.
# If both conditions are met, we return True. If we finish iterating through the array without finding such a pair, we return False.
#----------------------------------------------------------------------------------------
