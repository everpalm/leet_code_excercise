'''
435. Non-overlapping Intervals
Medium

Topics
Companies
Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest of
the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are
non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals
non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're
already non-overlapping.
 
Constraints:
1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
'''
class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        # Sort the intervals based on their end time
        intervals.sort(key=lambda x: x[1])

        # Initialize the end time of the last added interval to the first interval's end time
        end = intervals[0][1]
        count = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                # Overlapping interval, needs to be removed
                count += 1
            else:
                # No overlap, update the end to be the end of the current interval
                end = intervals[i][1]

        return count

# 測試用例
def test_solution():
    sol = Solution()
    assert sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1, "Test case 1 failed"
    assert sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2, "Test case 2 failed"
    assert sol.eraseOverlapIntervals([[1,2],[2,3]]) == 0, "Test case 3 failed"
    assert sol.eraseOverlapIntervals([]) == 0, "Test case 4 failed"
    assert sol.eraseOverlapIntervals([[1,3],[2,4],[3,5],[4,6]]) == 2, "Test case 5 failed"
    print("All test cases passed.")

test_solution()

