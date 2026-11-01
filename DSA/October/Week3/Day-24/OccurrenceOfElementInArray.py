# Week 3 - Day 24 - Problem: 3159. Find Occurrences of an Element in an Array
# ----------------------------------------------------------------------------------------
# Given an integer array nums and an integer target, return the number of occurrences of target in nums.
# You must write an algorithm with O(log n) runtime complexity.
# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i], target <= 10^9
# ----------------------------------------------------------------------------------------

def countOccurrences(nums, target):
    def findFirst():
        left, right = 0, len(nums) - 1
        first_occurrence = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first_occurrence = mid
                right = mid - 1  # Continue searching in the left half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return first_occurrence

    def findLast():
        left, right = 0, len(nums) - 1
        last_occurrence = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                last_occurrence = mid
                left = mid + 1  # Continue searching in the right half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return last_occurrence

    first_index = findFirst()
    if first_index == -1:  # Target not found
        return 0

    last_index = findLast()
    return last_index - first_index + 1

if __name__ == "__main__":
    # Test cases
    nums1 = [1, 2, 2, 2, 3, 4]
    target1 = 2
    print(countOccurrences(nums1, target1))  # Output: 3

    nums2 = [1, 1, 2, 3, 4]
    target2 = 5
    print(countOccurrences(nums2, target2))  # Output: 0

    nums3 = [5, 5, 5, 5]
    target3 = 5
    print(countOccurrences(nums3, target3))  # Output: 4

    nums4 = [1, 2, 3, 4]
    target4 = 4
    print(countOccurrences(nums4, target4))  # Output: 1


# ----------------------------------------------------------------------------------------
# Time complexity: O(log n), as we perform binary search twice (once for first occurrence and once for last occurrence).
# Space complexity: O(1), as we use a constant amount of space.
# Pattern: Boundary Binary Search
# How it works:
# We perform two binary searches: one to find the first occurrence of the target and another to find the last occurrence. The difference between the indices of the last and first occurrences gives us the count of the target in the array.
# ----------------------------------------------------------------------------------------