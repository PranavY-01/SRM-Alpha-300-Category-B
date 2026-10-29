# Week 4 - Day 29 - Problem: 435. Non-overlapping Intervals
# ----------------------------------------------------------------------------------------
# Given an array of intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Constraints:
# 1 ≤ intervals.length ≤ 10^5
# intervals[i].length == 2
# -5 * 104 <= start_i < end_i <= 5 * 104
# ----------------------------------------------------------------------------------------

def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    # Sort intervals using manual Merge Sort
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add any remaining intervals from the left and right lists
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    intervals = merge_sort(intervals)

    count = 0
    end = intervals[0][1]

    for i in range(1, len(intervals)):  # For each interval, check if it overlaps with the previous one
        if intervals[i][0] < end:
            count += 1  # Remove the overlapping interval
        else:
            end = intervals[i][1]  
    return count


if __name__ == "__main__":
    # Test cases
    intervals1 = [[1,2],[2,3],[3,4],[1,3]]
    print(eraseOverlapIntervals(intervals1))  # Output: 1

    intervals2 = [[1,2],[1,2],[1,2]]
    print(eraseOverlapIntervals(intervals2))  # Output: 2

    intervals3 = [[1,2],[2,3]]
    print(eraseOverlapIntervals(intervals3))  # Output: 0