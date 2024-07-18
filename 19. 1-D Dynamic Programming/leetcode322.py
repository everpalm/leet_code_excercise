'''
322. Coin Change
Medium

Topics
Companies
You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If
that amount of money cannot be made up by any combination of the coins,
return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
 

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''
class Solution:
    def coinChange(self, coins, amount):
        # Initialize dp array with infinity
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # base case: 0 coins needed to make amount 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

# Example usage:
solution = Solution()

coins1 = [1, 2, 5]
amount1 = 11
print(solution.coinChange(coins1, amount1))  # Output: 3

coins2 = [2]
amount2 = 3
print(solution.coinChange(coins2, amount2))  # Output: -1

coins3 = [1]
amount3 = 0
print(solution.coinChange(coins3, amount3))  # Output: 0
