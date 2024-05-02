'''
121. Best Time to Buy and Sell Stock
Easy

Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.

 
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        profit = max_profit = 0
        # while right < len(prices):
        for right in range(len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return 0 if max_profit < 0 else max_profit
        # if not prices:
        #     return 0  # Return 0 if the list is empty
        # min_price = prices[0]  # Initialize min_price with the first stock price
        # max_profit = 0  # Initialize max_profit as 0
        # for price in prices:
        #     # Update max_profit if selling at the current price yields a better profit
        #     max_profit = max(max_profit, price - min_price)
        #     # Update min_price if the current price is lower
        #     min_price = min(min_price, price)
        # return max_profit
            

my_solution = Solution()
prices = [7,1,5,3,6,4]
print(f'Result1 = {my_solution.maxProfit(prices)}')

prices = [7,6,4,3,1]
print(f'Result2 = {my_solution.maxProfit(prices)}')

prices = [2,1,4]
print(f'Result3 = {my_solution.maxProfit(prices)}')