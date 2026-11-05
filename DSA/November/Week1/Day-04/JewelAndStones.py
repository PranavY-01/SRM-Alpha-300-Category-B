# DSA Daily Gym | November | Week 1 | Day 4 | Problem: 771. Jewels and Stones
# --------------------------------------------------------------------------------------
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
# Constraints:
# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.
# --------------------------------------------------------------------------------------

def numJewelsInStones(jewels, stones):
    jewel_set = set(jewels)
    count = 0

    for stone in stones:
        if stone in jewel_set:
            count += 1

    return count

if __name__ == "__main__":
    # test cases
    jewels1 = "aA"
    stones1 = "aAAbbbb"
    print(numJewelsInStones(jewels1, stones1))  # Output: 3

    jewels2 = "z"
    stones2 = "ZZ"
    print(numJewelsInStones(jewels2, stones2))  # Output: 0

# --------------------------------------------------------------------------------------
# Time Complexity: O(n + m), where n is the length of jewels and m is the length of stones
# Space Complexity: O(n), for the jewel_set
# Pattern: Hash Set - Membership Checking
# --------------------------------------------------------------------------------------