# Week 4 - Day 28 - Problem: Allocate Minimum Pages (from GeeksForGeeks)
# ----------------------------------------------------------------------------------------
# Given an array arr[] of integers, where each element arr[i] represents the number of pages in the i-th book. 
# You also have an integer k representing the number of students. The task is to allocate books to each student such that:
# 1. Each student receives atleast one book.
# 2. Each student is assigned a contiguous sequence of books.
# 3. No book is assigned to more than one student.
# 4. All books must be allocated.
# The goal is to minimize the maximum number of pages assigned to a student. Return the minimum possible value of the maximum number of pages assigned to a student.
# Constraints:
# 1 ≤ arr.size() ≤ 106
# 1 ≤ arr[i], k ≤ 104
# ----------------------------------------------------------------------------------------

def isPossible(arr, n, k, mid):  # helper fn: to check if it is possible to allocate books such that the maximum number of pages assigned to a student is less than or equal to mid
    students_required = 1
    current_sum = 0

    for i in range(n):
        if arr[i] > mid:
            return False

        if current_sum + arr[i] > mid:
            students_required += 1
            current_sum = arr[i]

            if students_required > k:
                return False
        else:
            current_sum += arr[i]

    return True


def allocateMinimumPages(arr, k):  # main function: to find the minimum possible value of the maximum number of pages assigned to a student
    n = len(arr)

    # Every student must receive at least one book
    if k > n:
        return -1

    # Binary-search range for the answer
    left = max(arr)
    right = sum(arr)
    answer = right

    while left <= right:
        mid = left + (right - left) // 2

        if isPossible(arr, n, k, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

if __name__ == "__main__":
    # Test cases
    arr1 = [12, 34, 67, 90]
    k1 = 2
    print(allocateMinimumPages(arr1, k1))  # Output: 113

    arr2 = [10, 20, 30, 40]
    k2 = 2
    print(allocateMinimumPages(arr2, k2))  # Output: 60

    arr3 = [5, 17, 100, 11]
    k3 = 4
    print(allocateMinimumPages(arr3, k3))  # Output: 100

# ----------------------------------------------------------------------------------------
# Time Complexity: O(n log m), where n is the number of books and m is the sum of pages in all books.
# Space Complexity: O(1)
# Pattern: Binary Search on 1D Array
# How it works: The algorithm uses binary search to find the minimum possible value of the maximum number of pages assigned to a student. 
# It checks if it is possible to allocate books such that the maximum number of pages assigned to a student is less than or equal to mid, 
# and adjusts the search space accordingly until it finds the optimal value.