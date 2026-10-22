# Week 4 - Day 22 - Problem: 278. First Bad Version
# ----------------------------------------------------------------------------------------
# Given n versions of a product numbered from 1 to n, find the first bad version.
# All versions after the first bad version are also bad.
# You are provided an API isBadVersion(version), which returns True if a version
# is bad and False otherwise. Minimize the number of API calls.
#
# Constraints:
# 1 <= bad <= n <= 2^31 - 1
# ----------------------------------------------------------------------------------------

def firstBadVersion(n):
    left = 1
    right = n

    while left < right:
        mid = left + (right - left) // 2

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

def isBadVersion(version):  # This function is pre-defined in the Leetcode problem. Here, I simulate it for testing purposes.
    return version >= bad


if __name__ == "__main__":
    # Test cases
    n1 = 5
    bad = 4
    print(firstBadVersion(n1))  # Output: 4

    n2 = 1
    bad = 1
    print(firstBadVersion(n2))  # Output: 1

# -----------------------------------------------------------------------------------------
# Time complexity: O(log n), where n is the total number of versions.
# Space complexity: O(1), as only a few pointers and variables are used.
# Pattern: Binary Search / First True Condition
# How it works: Initialize two pointers representing the first and last versions.
# Check the middle version using the isBadVersion() API.
# If the middle version is bad, the first bad version must be at or before it,
# so move the right pointer to mid. Otherwise, move left to mid + 1.
# Continue until both pointers meet at the first bad version.
# -----------------------------------------------------------------------------------------
