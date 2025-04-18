'''
494. Target Sum
Medium

Topics
Companies
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+'
 and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates
to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5

Explanation: There are 5 ways to assign symbols to make the sum of nums be
target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1
 
Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        def dfs(index: int, current_sum: int) -> int:
            if index == n:
                return 1 if current_sum == target else 0
            
            # 選擇 +nums[index] 或 -nums[index]
            return (
                dfs(index + 1, current_sum + nums[index]) +
                dfs(index + 1, current_sum - nums[index])
            )
        
        return dfs(0, 0)
    
    def recursive_memory(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {0: 1}
        for num in nums:
            temp = {}
            for d, count in dp.items():
                temp[d + num] = temp.get(d + num, 0) + count
                temp[d - num] = temp.get(d - num, 0) + count
            dp = temp
        return dp.get(target, 0)
    
    def dynamic_programming(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        # 特判：若 |target| > total 或 (total + target) 為奇數，則不存在合法解
        if abs(target) > total or (total + target) % 2 != 0:
            return 0
        
        subsetSum = (total + target) // 2
        
        # 初始化 dp 陣列，dp[i] 表示組合出 i 的方案數
        dp = [0] * (subsetSum + 1)
        dp[0] = 1
        
        # 遍歷每個數字，更新 dp 陣列
        for num in nums:
            for i in range(subsetSum, num - 1, -1):
                dp[i] += dp[i - num]
        
        return dp[subsetSum]

if __name__ == '__main__':  
    sol = Solution()
    nums = [1,1,1,1,1]
    target = 3
    print("Example1 = ", sol.findTargetSumWays(nums, target))  # Expected 5
    print("Example1 = ", sol.dynamic_programming(nums, target))  # Expected 5

    nums = [1]
    target = 1
    print("Example2 = ", sol.findTargetSumWays(nums, target))  # Expected 1
    print("Example2 = ", sol.dynamic_programming(nums, target))  # Expected 1

