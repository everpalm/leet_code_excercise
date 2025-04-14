'''
518. Coin Change II
Medium

Topics
Companies
You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of
money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1
 

Constraints:
1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
'''
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(index: int, current: int) -> int:
            # 如果当前金额正好等于目标金额，找到一种合法组合
            if current == amount:
                return 1
            # 如果当前金额超过目标金额，或没有硬币可用，则无法组成目标金额
            if current > amount or index == len(coins):
                return 0
            
            count = 0
            coin_value = coins[index]
            # 尝试使用 k 个当前硬币，只要总金额不超过目标
            k = 0
            while current + k * coin_value <= amount:
                count += dfs(index + 1, current + k * coin_value)
                k += 1
            return count

        return dfs(0, 0)
    
    def dynamic_programming(self, amount: int, coins: List[int]) -> int:
        # 初始化 dp 陣列，dp[i] 表示凑出金額 i 的組合數，初始全為 0
        dp = [0] * (amount + 1)
        dp[0] = 1  # 凑出 0 金額只有一種方法：不選任何硬幣

        # 遍歷每一種硬幣
        for coin in coins:
            # 對每個硬幣，從 coin 到 amount 更新 dp 值
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        
        return dp[amount]

if __name__ == '__main__':  
    sol = Solution()
    amount = 5
    coins = [1,2,5]
    print(sol.change(amount, coins))  # Expected 4
    print(sol.dynamic_programming(amount, coins))  # Expected 4

    amount = 3
    coins = [2]
    print(sol.change(amount, coins))  # Expected 0
    print(sol.dynamic_programming(amount, coins))  # Expected 4

    amount = 10
    coins = [10]
    print(sol.change(amount, coins))  # Expected 1
    print(sol.dynamic_programming(amount, coins))  # Expected 4