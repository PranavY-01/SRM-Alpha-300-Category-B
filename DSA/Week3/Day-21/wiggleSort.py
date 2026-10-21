# Week 3 - Day 21 - Problem: 321. Wiggle Sort
# ----------------------------------------------------------------------------------------
# Given an integer array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
# You may assume the input array always has a valid answer.
# Constraints:
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
# ----------------------------------------------------------------------------------------

def wiggleSort(nums):
        v = sorted(nums)
        n = len(nums)

        mid = (n + 1) // 2
        left = mid - 1
        right = n - 1

        for i in range(n):
            if i % 2 == 0:
                nums[i] = v[left]
                left -= 1
            else:
                nums[i] = v[right]
                right -= 1

        return nums

if __name__ == "__main__":
    # Test cases
    nums1 = [1, 5, 1, 1, 6, 4]
    print(wiggleSort(nums1))  # Output: [1, 6, 1, 5, 1, 4]

    nums2 = [1, 3, 2, 2, 3, 1]
    print(wiggleSort(nums2))  # Output: [2, 3, 1, 3, 1, 2]

# -----------------------------------------------------------------------------------------
# Time complexity: O(n log n) where n is the number of elements in the input array.
# Space complexity: O(n) as we are using an additional array to store the sorted values.
# Pattern: Sorting and Rearranging
# How it works: This implementation first sorts the input array and then rearranges the elements in a wiggle pattern.
# The left pointer starts from the middle of the sorted array and fills the even indices, while the right pointer starts from the end of the sorted array and fills the odd indices.
# This ensures that the wiggle property is maintained, with nums[0] <= nums[1] >= nums[2] <= nums[3]....
# -----------------------------------------------------------------------------------------
        