# Week 4 - Day 29 - Problem: 56. Merge Intervals
# ----------------------------------------------------------------------------------------
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Constraints:
# 1 ≤ intervals.length ≤ 10^4
# 0 ≤ starti ≤ endi ≤ 10^4
# ----------------------------------------------------------------------------------------

def merge(intervals):  # Sort intervals using a manually implemented Merge Sort
    
    def merge_sorted(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge_sorted(left, right)

    intervals = merge_sort(intervals)
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval[:])
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

if __name__ == "__main__":
    # Test cases
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(merge(intervals1))  # Output: [[1, 6], [8, 10], [15, 18]]

    intervals2 = [[1, 4], [4, 5]]
    print(merge(intervals2))  # Output: [[1, 5]]

    intervals3 = [[4,7],[1,4]]
    print(merge(intervals3))  # Output: [[1, 7]]

