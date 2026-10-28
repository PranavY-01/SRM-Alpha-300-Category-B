# week 4 - Day 28 - Problem: 875. Koko Eating Bananas
# ----------------------------------------------------------------------------------------
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during that hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return. Return the minimum integer k such that she can eat all the bananas within h hours.
# Constraints:
# 1 <= piles.length <= 10^4
# piles.length <= h <= 10^9
# 1 <= piles[i] <= 10^9
# ----------------------------------------------------------------------------------------

def minEatingSpeed(piles, h):
    left, right = 1, max(piles)

    while left < right:
        mid = left + (right - left) // 2
        required_hours = sum((pile + mid - 1) // mid for pile in piles)

        if required_hours > h:
            left = mid + 1
        else:
            right = mid

    return left

if __name__ == "__main__":
    # Test cases
    piles1 = [3, 6, 7, 11]
    h1 = 8
    print(minEatingSpeed(piles1, h1))  # Output: 4

    piles2 = [30, 11, 23, 4, 20]
    h2 = 5
    print(minEatingSpeed(piles2, h2))  # Output: 30

    piles3 = [30, 11, 23, 4, 20]
    h3 = 6
    print(minEatingSpeed(piles3, h3))  # Output: 23

# ----------------------------------------------------------------------------------------
# Time Complexity: O(n log m), where n is the number of piles and m is the maximum number of bananas in a pile.
# Space Complexity: O(1)
# Pattern: Binary Search on 1D Array
# How it works: The algorithm uses binary search to find the minimum eating speed k. It calculates the required hours for each mid value 
# and adjusts the search space accordingly until it finds the optimal k.
# ----------------------------------------------------------------------------------------