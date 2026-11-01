# Week 3 - Day 18 - Problem: 3193. Count the Number of Inversions
# ----------------------------------------------------------------------------------------
# You are given an integer n and a 2D array requirements, where requirements[i] = [endi, cnti] represents the end index and the inversion count of each requirement.
# A pair of indices (i, j) from an integer array nums is called an inversion if: i < j and nums[i] > nums[j]
# Return the number of permutations perm of [0, 1, 2, ..., n - 1] such that for all requirements[i], perm[0..endi] has exactly cnti inversions.
# Since the answer may be very large, return it modulo 109 + 7.
# Constraints:
# 1 <= arr.length <= 10^5
# -10^9 <= arr[i] <= 10^9
# ----------------------------------------------------------------------------------------

def countInversions(arr):
    def merge_sort(arr, left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2

        count = merge_sort(arr, left, mid)
        count += merge_sort(arr, mid + 1, right)
        count += merge(arr, left, mid, right)

        return count

    def merge(arr, left, mid, right):
        temp = []
        i = left
        j = mid + 1
        count = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                count += mid - i + 1
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= right:
            temp.append(arr[j])
            j += 1

        for k in range(len(temp)):
            arr[left + k] = temp[k]

        return count

    return merge_sort(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    # Test cases
    arr1 = [2, 4, 1, 3, 5]
    print(countInversions(arr1))  # Output: 3

    arr2 = [5, 4, 3, 2, 1]
    print(countInversions(arr2))  # Output: 10

# -----------------------------------------------------------------------------------------
# Time complexity: O(n log n) where n is the length of the input array.
# Space complexity: O(n) as we are using additional space for the temporary array during the merge process.
# Pattern: Divide and Conquer Approach
# How it works: This implementation uses a modified merge sort algorithm to count the number of inversions in an array. It recursively divides the array into halves, counts the inversions in each half, and then counts the inversions that span across the two halves during the merge process.
# -----------------------------------------------------------------------------------------
