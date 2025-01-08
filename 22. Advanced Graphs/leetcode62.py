'''
62. Unique Paths
Medium

Topics
Companies
There is a robot on an m x n grid. The robot is initially located at the
top-left corner (i.e., grid[0][0]). The robot tries to move to the
bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either
down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to
2 * 109.
 
Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3

m = 2, n = 2
0,0 -> 0,1 -> 1,1
0,0 -> 1,0 -> 1,1

m = 3, n = 2
0,0 -> 0,1 -> 1,1 -> 2,1
0,0 -> 1,0 -> 1,1 -> 2,1
0,0 -> 1,0 -> 2,0 -> 2,1

m = 4, n = 2
0,0 -> 0,1 -> 1,1 -> 2,1 -> 3,1
0,0 -> 1,0 -> 1,1 -> 2,1 -> 3,1
0,0 -> 1,0 -> 2,0 -> 3,0 -> 3,1
0,0 -> 1,0 -> 2,0 -> 2,1 -> 3,1

Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 
Constraints:
1 <= m, n <= 100
'''
class Solution:
    def brute_force(self, m: int, n: int) -> int:
        def count_paths(x, y):
            # 基礎情況：到達右下角
            if x == m - 1 and y == n - 1:
                return 1
            # 超出邊界
            if x >= m or y >= n:
                return 0
            
            # 向下和向右的路徑數量
            return count_paths(x + 1, y) + count_paths(x, y + 1)

        return count_paths(0, 0) 

    def dynamic_programming(self, m: int, n: int) -> int:
        # 創建一個 m x n 的 dp 陣列
        dp = [[1] * n for _ in range(m)]
        
        # 填充 dp 陣列
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1] 
    
solution = Solution()
# print('solution1 = ', solution.brute_force(3, 7))
print('solution2 = ', solution.brute_force(3, 2))
print('solution3 = ', solution.dynamic_programming(3, 2))