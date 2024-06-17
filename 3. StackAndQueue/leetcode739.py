'''
739. Daily Temperatures
Medium

Topics
Companies

Hint
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to
wait after the ith day to get a warmer temperature. If there is no future day
for which this is possible, keep answer[i] == 0 instead.

 
Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List) -> List:
        n = len(temperatures)
        result = [0] * n
        
        # Stack to keep the indices of the temperatures array
        stack = []
        # Iterate over the array
        for i in range(n):
            # print(f'temperatures[{i}] = {temperatures[i]}')
            if stack: print(f'\nstack[-1] = {stack[-1]}')
            print(f'temperatures[{i}] = {temperatures[i]}')
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                print('index = ', index)
                result[index] = i - index
                # print(f'{i}th result = {result[index]}')
            stack.append(i)
            print(f'\n{i}th stack = ', stack)
        return result
    

my_solution = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print('Result1 = ', my_solution.dailyTemperatures(temperatures))
temperatures = [30,40,50,60]
print('Result2 = ', my_solution.dailyTemperatures(temperatures))
temperatures = [30,60,90]
print('Result3 = ', my_solution.dailyTemperatures(temperatures))