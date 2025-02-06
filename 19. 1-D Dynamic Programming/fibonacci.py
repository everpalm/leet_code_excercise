class Solution:
    def classic(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # 創建 dp 陣列
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        # 填充 dp 陣列
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]  # 返回第 n 個費波那契數

    def advanced(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        a, b = 0, 1  # 初始化前兩個費波那契數
        for _ in range(2, n + 1):
            a, b = b, a + b  # 更新前兩個數

        return b  # 返回第 n 個費波那契數

solution = Solution()

# 測試
print("classic: ", solution.classic(10))  # 輸出: 55

# 測試
print("advanced: ", solution.advanced(10))  # 輸出: 55