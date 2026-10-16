# Week 2 - Day 16 - Problem 378. Kth Smallest Element in a Sorted Matrix
# ----------------------------------------------------------------------------------------
# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
# You must find a solution with a memory complexity better than O(n2).
#
# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 300
# -109 <= matrix[i][j] <= 109
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n^2
# ----------------------------------------------------------------------------------------

def kthSmallest(matrix, k):
    n = len(matrix)

    low = matrix[0][0]
    high = matrix[n - 1][n - 1]

    while low < high:          # Count number of elements less than or equal to mid and adjust the search range
        mid = (low + high) // 2
        count = 0

        for row in matrix:   # Count the number of elements less than or equal to mid
            for num in row:
                if num <= mid:
                    count += 1

        if count < k:  # Classic binary search adjustment
            low = mid + 1
        else:
            high = mid

    return low

if __name__ == "__main__":
    # Test cases
    matrix1 = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k1 = 8
    print(kthSmallest(matrix1, k1))  # Output: 13

    matrix2 = [[-5]]
    k2 = 1
    print(kthSmallest(matrix2, k2))  # Output: -5