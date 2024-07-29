'''
56. Merge Intervals
Classic!

Medium

Topics
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''
from typing import List


class Solution:
    # def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
    #     n = len(intervals)
    #     i = 0
    #     result = []
    #     prev = intervals[0]
    #     curr = intervals[1]

    #     while i < n and curr[0] > prev[1]:
    #         result.append(curr)
    #         i += 1
    #         prev = curr
    #         curr = intervals[i]

    #     prev = intervals[0]
    #     curr = intervals[1]
    #     while i < n and curr[1] <= prev[0]:
    #         curr[0] = min(curr[0], intervals[i][0])
    #         curr[1] = max(curr[1], intervals[i][1])
    #         i += 1
    #         prev = curr
    #         curr = intervals[i]

    #     while i < n:
    #         result.append(intervals[i])
    #         i += 1

        # return result
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Initialize a list to hold merged intervals
        merged = []
        
        for interval in intervals:
            # If the merged list is empty or if the current interval does not overlap with the previous, append it
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # If it does overlap, merge the current interval with the previous one
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
    

solution =Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
# print('Result1 = ', solution.merge(intervals))
print('Result1 = ', solution.merge(intervals))

intervals = [[1,4],[4,5]]
print('Result2 = ', solution.merge(intervals))

