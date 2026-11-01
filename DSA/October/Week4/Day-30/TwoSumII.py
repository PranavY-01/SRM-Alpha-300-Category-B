# Week 4 - Day 30: Problem: 167. Two Sum II - Input Array Is Sorted
# ----------------------------------------------------------------------------------------
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Constraints:
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# ----------------------------------------------------------------------------------------

def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # Return 1-indexed positions
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [] # clean retrun if no solution is found.

if __name__ == "__main__":
    # Test cases
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    print(twoSum(numbers1, target1))  # Output: [1, 2]

    numbers2 = [2, 3, 4]
    target2 = 6
    print(twoSum(numbers2, target2))  # Output: [1, 3]

    numbers3 = [-1, 0]
    target3 = -1
    print(twoSum(numbers3, target3))  # Output: [1, 2]

# ----------------------------------------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Pattern: Two Pointers
# How it works: The algorithm uses two pointers, one starting at the beginning of the array and the other at the end. 
# It calculates the sum of the two numbers at these pointers and adjusts the pointers based on 
# whether the sum is less than or greater than the target, until it finds the pair that adds up to the target.
# ----------------------------------------------------------------------------------------