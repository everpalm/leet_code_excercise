'''
253. Meeting Schedule II

Classic Greedy algorithm!

Given an array of meeting time interval objects consisting of start and end
times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the
minimum number of days required to schedule all meetings without any conflicts
.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]
Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:
Input: intervals = [(4,9)]
Output: 1
Note:
(0,8),(8,10) is not considered a conflict at 8

Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
'''
from typing import List
import heapq

class Solution:
    def minMeetingDays(self, intervals: List[tuple[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals by start time (and by end time in case of a tie)
        intervals.sort(key=lambda x: (x[0], x[1]))

        # List to track the end times of meetings scheduled on each day
        end_times = []

        for interval in intervals:
            placed = False
            for i in range(len(end_times)):
                if interval[0] >= end_times[i]:
                    # If the meeting can be placed on this day
                    end_times[i] = interval[1]
                    placed = True
                    break
            if not placed:
                # If it couldn't be placed on any existing day, schedule a new day
                end_times.append(interval[1])

        # The number of days required is the length of the end_times list
        return len(end_times)


    def minMeetingDays1(self, intervals):
        if not intervals:
            return 0

        # 先按照開始時間排序，如果開始時間相同，則按結束時間排序
        intervals.sort(key=lambda x: (x[0], x[1]))

        # 使用最小堆來跟蹤每一天的最後一個會議的結束時間
        min_heap = []

        for interval in intervals:
            if min_heap and interval[0] >= min_heap[0]:
                # 如果當前會議的開始時間大於或等於最小堆頂的結束時間
                # 更新最小堆頂的結束時間為當前會議的結束時間
                heapq.heapreplace(min_heap, interval[1])
            else:
                # 無法放在任何已存在的天，需要新增加一天
                heapq.heappush(min_heap, interval[1])

        # 最小堆的大小就是所需的最少天數
        return len(min_heap)
    

# Example usage
solution = Solution()
intervals1 = [(0, 40), (5, 10), (15, 20)]
intervals2 = [(4, 9)]
print(solution.minMeetingDays(intervals1))  # Output: 2
print(solution.minMeetingDays(intervals2))  # Output: 1
