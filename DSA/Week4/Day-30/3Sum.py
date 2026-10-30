# Week 4 - Day 30 - Problem: 15. 3Sum
# ----------------------------------------------------------------------------------------
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Constraints:
# 0 ≤ nums.length ≤ 3000
# -10^5 ≤ nums[i] ≤ 10^5
# ----------------------------------------------------------------------------------------

def threeSum(nums):
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    nums = merge_sort(nums)

    # Step 2: Two-pointer approach
    result = []
    n = len(nums)

    for i in range(n - 2):

        # Skip duplicate first elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # No possible triplet if the smallest value is positive
        if nums[i] > 0:
            break

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1

            elif total > 0:
                right -= 1

            else:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                # Skip duplicate second elements
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicate third elements
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result

if __name__ == "__main__":
    # Test cases
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums1))  # Output: [[-1, -1, 2], [-1, 0, 1]]

    nums2 = [0, 1, 1]
    print(threeSum(nums2))  # Output: []

    nums3 = [0, 0, 0]
    print(threeSum(nums3))  # Output: [[0, 0, 0]]