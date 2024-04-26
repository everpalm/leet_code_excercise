'''
22. Generate Parentheses
Medium

Topics
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
class Solution:
    def generateParenthesis(self, n: int) -> list:
        def backtrack(current, open_count, close_count):
            print(f'n = {n}, current = {current}, open_count = {open_count}, close_count = {close_count}')
            if len(current) == 2 * n:
                results.append(current)
                return
            
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
    
        results = []
        backtrack('', 0, 0)
        return results


my_solution = Solution()
print('Result1 = ', my_solution.generateParenthesis(3))
print('Result2 = ', my_solution.generateParenthesis(1))