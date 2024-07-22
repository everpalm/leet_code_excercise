'''
300. Longest Increasing Subsequence
Medium

Topics
Companies
Given an integer array nums, return the length of the longest strictly
increasing subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 
Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
complexity?
'''
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]):
        from bisect import bisect_left

        if not nums:
            return 0

        dp = []
        for num in nums:
            index = bisect_left(dp, num)
            if index == len(dp):
                dp.append(num)
            else:
                dp[index] = num

        return len(dp)

# Test cases
solution = Solution()
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4
print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))           # Output: 4
print(solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))        # Output: 1
