# DSA Daily Gym | November | Week 2 | Day 11 | Problem: 1260. Shift 2D Grid
# --------------------------------------------------------------------------------------
# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
# In one shift operation:
# 1. Element at grid[i][j] moves to grid[i][j + 1].
# 2. Element at grid[i][n - 1] moves to grid[i + 1][0].
# 3. Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.
# Constraints:
# 1 <= m <= 50
# 1 <= n <= 50
# 1 <= k <= 100
# -1000 <= grid[i][j] <= 1000
# --------------------------------------------------------------------------------------

def shiftGrid(grid, k):
    m, n = len(grid), len(grid[0])
    total_elements = m * n
    k = k % total_elements  # To handle cases where k is larger than total elements

    # Flatten the grid into a 1D list
    flat_list = [grid[i][j] for i in range(m) for j in range(n)]
    
    # Shift the flat list
    shifted_list = flat_list[-k:] + flat_list[:-k]
    
    # Convert back to 2D grid
    new_grid = [[0] * n for _ in range(m)]
    for i in range(total_elements):
        new_grid[i // n][i % n] = shifted_list[i]
    
    return new_grid

if __name__ == "__main__":
    # test cases
    grid1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k1 = 1
    print(shiftGrid(grid1, k1))  # Output: [[9, 1, 2], [3, 4, 5], [6, 7, 8]]

    grid2 = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
    k2 = 4
    print(shiftGrid(grid2, k2))  
    # Output: [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]

    grid3 = [[1], [2], [3], [4], [7], [6], [5]]
    k3 = 23
    print(shiftGrid(grid3, k3))  
    # Output: [[6], [5], [1], [2], [3], [4], [7]]

# --------------------------------------------------------------------------------------
# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid.
# Space Complexity: O(m * n) for the flattened list and the new grid.
# Pattern: Array Manipulation, 2D Array
# --------------------------------------------------------------------------------------
