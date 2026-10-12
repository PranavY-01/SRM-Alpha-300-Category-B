# Week-2 Day -12: 904. Fruit Into Baskets
# ---------------------------------------------------------------------------------------- 
# You are visiting a farm that has a single row of fruit trees arranged from left to right.
# The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree.
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
# 
# 1. You only have two baskets, and each basket can only hold a single type of fruit. 
# There is no limit on the amount of fruit each basket can hold.
# 
# 2. Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right.
# The picked fruits must fit in one of your baskets. 
# 
# 3. Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# 
# Given the integer array fruits, return the maximum number of fruits you can pick. 
# 
# Constraints:
# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length
# ----------------------------------------------------------------------------------------

def totalFruit(fruits):
    max_fruits = 0
    left = 0
    fruit_count = {}

    for right in range(len(fruits)):
        fruit = fruits[right]
        fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

        while len(fruit_count) > 2:
            left_fruit = fruits[left]
            fruit_count[left_fruit] -= 1
            if fruit_count[left_fruit] == 0:
                del fruit_count[left_fruit]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)
    return max_fruits

if __name__ == "__main__":
    fruits = [1, 2, 1]
    print(totalFruit(fruits))  # Output: 3

    fruits = [0, 1, 2, 2]
    print(totalFruit(fruits))  # Output: 3

    fruits = [1, 2, 3, 2, 2]
    print(totalFruit(fruits))  # Output: 4

# ----------------------------------------------------------------------------------------
# Time complexity: O(n)
# Space complexity: O(1) (since the number of unique fruits is limited to 2)
# Pattern: Sliding Window with Hash Map
# How it works: We use a sliding window approach with two pointers (left and right) to maintain a window of fruits.
# We use a hash map to count the occurrences of each fruit type in the current window.
# If the number of unique fruit types exceeds 2, we shrink the window from the left 
# until we have at most 2 unique types.
# We keep track of the maximum window size encountered during the process, 
# which represents the maximum number of fruits we can pick.
#----------------------------------------------------------------------------------------