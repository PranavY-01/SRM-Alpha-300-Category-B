# Week 4 - Day 24 - Problem: 34. Find First and Last Position of Element in Sorted Array
# ----------------------------------------------------------------------------------------
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# Constraints:
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# ----------------------------------------------------------------------------------------

def searchRange(nums, target):

    def findFirst():   # Find the first occurrence of the target
        left = 0
        right = len(nums) - 1
        answer = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                answer = mid
                right = mid - 1  # Continue searching left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return answer

    def findLast():   # Find the last occurrence of the target  
        left = 0
        right = len(nums) - 1
        answer = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                answer = mid
                left = mid + 1  # Continue searching right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return answer

    first = findFirst()  

    if first == -1:  # Target not found, return [-1, -1]
        return [-1, -1]

    last = findLast()

    return [first, last]


if __name__ == "__main__":
    print(searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
    print(searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
    print(searchRange([], 0))                   # [-1, -1]

# ----------------------------------------------------------------------------------------
# Time complexity: O(log n)
# Auxiliary space: O(1)
# Pattern: Boundary Binary Search
# No bisect_left(), bisect_right(), sorted(), or .sort()
# ----------------------------------------------------------------------------------------