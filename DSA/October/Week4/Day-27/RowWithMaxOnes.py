# Week 4 - Day 27 - Problem: 2643. Row With Maximum Ones (using Binary Search)
# ----------------------------------------------------------------------------------------
# Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.
# In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.
# Return an array containing the index of the row, and the number of ones in it.
# Constraints:
# m == mat.length 
# n == mat[i].length
# 1 <= m, n <= 100
# mat[i][j] is either 0 or 1.
# ----------------------------------------------------------------------------------------

def rowWithMaxOnes(mat):
    max_i = -1
    max_c = 0

    for i in range(len(mat)):
        left, right = 0, len(mat[i]) 

        while left < right:               # Find the first occurrence of 1
            mid = left + (right - left) // 2

            if mat[i][mid] == 1:
                right = mid
            else:
                left = mid + 1

        count = len(mat[i]) - left        # Number of ones = columns - first index of 1

        if count > max_c:
            max_c = count
            max_i = i

    return [max_i, max_c] if max_i != -1 else [-1, 0]

if __name__ == "__main__":
    # Test cases
    mat1 = [
        [0, 1, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ]
    print(rowWithMaxOnes(mat1))  # Output: [2, 4]

    mat2 = [
        [0, 0],
        [0, 0]
    ]
    print(rowWithMaxOnes(mat2))  # Output: [-1, 0]

# ----------------------------------------------------------------------------------------
# Time Complexity: O(m * n) where m is the number of rows and n is the number of columns
# Space Complexity: O(1)
# Pattern: Iteration and Counting
# How it works: The algorithm iterates through each row of the binary matrix, counts the number of ones in that row, and keeps track of the row index with the maximum count of ones. If multiple rows have the same maximum count, the first one encountered is selected.
# ----------------------------------------------------------------------------------------
