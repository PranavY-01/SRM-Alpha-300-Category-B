# Week 4 - Day 29 - Probelm: 57. Insert Interval
# ----------------------------------------------------------------------------------------
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the i-th interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Constraints:
# 0 ≤ intervals.length ≤ 10^4
# 0 ≤ starti ≤ endi ≤ 10^4
# ----------------------------------------------------------------------------------------

def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals that come before the new interval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals with the new interval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    result.append(newInterval)

    # Add all remaining intervals after the new interval
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

if __name__ == "__main__":
    # Test cases
    intervals1 = [[1,3],[6,9]]
    newInterval1 = [2,5]
    print(insert(intervals1, newInterval1))  # Output: [[1, 5], [6, 9]]

    intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval2 = [4,8]
    print(insert(intervals2, newInterval2))  # Output: [[1, 2], [3, 10], [12, 16]]

# ----------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the number of intervals in the input list. We iterate through the list of intervals once to insert the new interval and merge any overlapping intervals.
# Space Complexity: O(n), where n is the number of intervals in the input list.
# Pattern: Two Pointers
# How it works: The algorithm uses two pointers to iterate through the list of intervals and insert the new interval while merging any overlapping intervals. It maintains a result list to store the final merged intervals.
# ----------------------------------------------------------------------------------------