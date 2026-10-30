# Week 4 - Day 30 - Problem: 128. Longest Consecutive Sequence
# ----------------------------------------------------------------------------------------
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# Constraints:
# 0 ≤ nums.length ≤ 10^5
# -10^9 ≤ nums[i] ≤ 10^9
# ----------------------------------------------------------------------------------------

def longestConsecutive(nums):  
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:  # only start counting if 'num' is the start of a sequence. failsafe (to avoid counting the same sequence multiple times)
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

if __name__ == "__main__":
    # Test cases
    nums1 = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(nums1))  # Output: 4 

    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(longestConsecutive(nums2))  # Output: 9 

    nums3 = [1, 0, 1, 2]
    print(longestConsecutive(nums3))  # Output: 3

# ----------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(n)
# Pattern: Hashing
# How it works: The algorithm uses a set to store the numbers and iterates through the set to find the longest consecutive sequence by checking for the start of each sequence.
# ----------------------------------------------------------------------------------------