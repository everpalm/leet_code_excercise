'''
252. Meeting Schedule
Easy
Given an array of meeting time interval objects consisting of start and end
times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a
person could add all meetings to their schedule without any conflicts.

Example 1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:
(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict

Example 2:
Input: intervals = [(5,8),(9,15)]
Output: true
Note:
(0,8),(8,10) is not considered a conflict at 8

Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
'''
class Solution:
    def can_attend_all_meetings(self, intervals):
        # Step 1: Sort the intervals by start times
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Check for overlaps
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        
        return True

    def can_attend_all_meetings1(self, intervals):
        # Step 1: Sort the intervals by start times
        intervals.sort(key=lambda x: x[0])
        end = intervals[0][1]
        # Step 2: Check for overlaps
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                return False
            else:
                end = intervals[i][1]
        
        return True
# Example usage:
solution = Solution()

# Example 1
intervals1 = [(0, 30), (5, 10), (15, 20)]
print(solution.can_attend_all_meetings1(intervals1))  # Output: False

# Example 2
intervals2 = [(5, 8), (9, 15)]
print(solution.can_attend_all_meetings1(intervals2))  # Output: True
