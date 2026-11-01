# Week 4 - Day 27 - Problem: 74. Search a 2D Matrix
# ----------------------------------------------------------------------------------------
# Given an m x n matrix, where each row is sorted in ascending order and the first integer of each row is greater than the last integer of the previous row, write an efficient algorithm that searches for a value in the matrix.
# The matrix has the following properties:
# 1. Integers in each row are sorted from left to right.
# 2. The first integer of each row is greater than the last integer of the previous row.
# Constraints:
# The matrix is sorted in ascending order and contains distinct elements.
# ----------------------------------------------------------------------------------------

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0]) 
    left, right = 0, rows * cols - 1

    while left <= right:   # basic binary search
        mid = left + (right - left) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

if __name__ == "__main__":
    # Test cases
    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target1 = 3
    print(searchMatrix(matrix1, target1))  # Output: True

    matrix2 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target2 = 13
    print(searchMatrix(matrix2, target2))  # Output: False

# ---------------------------------------------------------------------------------------- 
# Time Complexity: O(log(m * n)) where m is the number of rows and n is the number of columns
# Space Complexity: O(1)
# Pattern: Binary Search on 2D Matrix
# How it works: The algorithm treats the 2D matrix as a 1D sorted array and applies binary search. It calculates the middle index and maps it back to the 2D coordinates to access the matrix elements. The search space is narrowed down based on comparisons with the target value.
# ----------------------------------------------------------------------------------------
