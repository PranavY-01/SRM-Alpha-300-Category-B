# Week 4 - Day 28 - Problem: 1011. Capacity To Ship Packages Within D Days
# ----------------------------------------------------------------------------------------
# A conveyor belt has packages that must be shipped from one port to another within days days.
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
# Constraints:
# 1 <= days <= weights.length <= 5 * 10^4
# 1 <= weights[i] <= 500
# ----------------------------------------------------------------------------------------

def shipWithinDays(weights, days):
    left, right = max(weights), sum(weights)

    while left < right:
        mid = left + (right - left) // 2
        required_days = 1
        current_weight = 0

        for weight in weights:
            if current_weight + weight > mid:
                required_days += 1
                current_weight = 0
            current_weight += weight

        if required_days > days:
            left = mid + 1
        else:
            right = mid

    return left

if __name__ == "__main__":
    # Test cases
    weights1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days1 = 5
    print(shipWithinDays(weights1, days1))  # Output: 15

    weights2 = [3, 2, 2, 4, 1, 4]
    days2 = 3
    print(shipWithinDays(weights2, days2))  # Output: 6

    weights3 = [1, 2, 3, 1, 1]
    days3 = 4
    print(shipWithinDays(weights3, days3))  # Output: 3