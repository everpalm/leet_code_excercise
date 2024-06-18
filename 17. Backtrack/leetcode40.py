'''
40. Combination Sum II
Medium

Topics
Companies
Given a collection of candidate numbers (candidates) and a target number
(target), find all unique combinations in candidates where the candidate
numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 
Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, path):
            current_sum = sum(path)
            # Base case 1
            if current_sum == target:
                result.append(path[:])
                return
            
            # Base case 2
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                # path.append(candidates[i])
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, path + [candidates[i]])
                # path.pop()

        candidates.sort()
        backtrack(0, [])
        return result


candidates = [10,1,2,7,6,1,5]
target = 8
solution = Solution()
print('Result1 = ', solution.combinationSum2(candidates, target))
print('\n')

candidates = [2,5,2,1,2]
target = 5
print('Result2 = ', solution.combinationSum2(candidates, target))
print('\n')

candidates = [2,5,2,1,2]
target = 5
print('Result3 = ', solution.combinationSum2(candidates, target))