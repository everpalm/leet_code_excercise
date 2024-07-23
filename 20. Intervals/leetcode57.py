'''
57. Insert Interval
Medium

Topics
Companies

Hint
You are given an array of non-overlapping intervals intervals where
intervals[i] = [starti, endi] represent the start and the end of the ith
interval and intervals is sorted in ascending order by starti. You are also
given an interval newInterval = [start, end] that represents the start and end
of another interval.

Insert newInterval into intervals such that intervals is still sorted in
ascending order by starti and intervals still does not have any overlapping
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new
array and return it.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 
Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
'''
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) \
        -> List[int]:
        result = []
        i = 0
        n = len(intervals)
        
        # Add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals with the new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # Add the merged interval
        result.append(newInterval)
        
        # Add the remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result

# 测试示例
solution = Solution()

intervals1 = [[1, 3], [6, 9]]
newInterval1 = [2, 5]
print(solution.insert(intervals1, newInterval1))  # 输出: [[1, 5], [6, 9]]

intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval2 = [4, 8]
print(solution.insert(intervals2, newInterval2))  # 输出: [[1, 2], [3, 10], [12, 16]]
