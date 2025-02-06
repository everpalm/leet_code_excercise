'''
309. Best Time to Buy and Sell Stock with Cooldown
Medium

Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on
the ith day.

Find the maximum profit you can achieve. You may complete as many transactions
as you like (i.e., buy one and sell one share of the stock multiple times)
with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e.,
cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you
must sell the stock before you buy again).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0
 
Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''
from typing import List


class Solution:
    def brute_force(self, prices: List[int]) -> int:
        def dfs(day, hasStock):
        # 基礎情況：如果超過價格數組的長度
            if day >= len(prices):
                return 0
            
            if hasStock:
                # 如果持有股票，可以選擇賣出或不操作
                sell = prices[day] + dfs(day + 2, False)  # 賣出，進入冷卻狀態
                hold = dfs(day + 1, True)  # 保持不變
                return max(sell, hold)
            else:
                # 如果不持有股票，可以選擇買入或不操作
                buy = -prices[day] + dfs(day + 1, True)  # 買入
                skip = dfs(day + 1, False)  # 保持不變
                return max(buy, skip)

        return dfs(0, False)  # 從第 0 天開始，不持有股票

# 測試
solution = Solution()
print(solution.brute_force([1, 2, 3, 0, 2]))  # 輸出: 3
print(solution.brute_force([1]))               # 輸出: 0