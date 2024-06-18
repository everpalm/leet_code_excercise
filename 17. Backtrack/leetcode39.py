''''
39. Combination Sum
Medium

Topics
Companies
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen
numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen
numbers is different.

The test cases are generated such that the number of unique combinations that
sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
 
Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
'''
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, path):
            current_sum = sum(path)
            # Base case 1
            if current_sum == target:
                result.append(path[:])
                # If not use copy of path, when pop path the last element that sums
                # up target will be removed
                # result.append(path)
                return
            
            # Base case 2
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path)
                path.pop()
        # 如果不对 candidates 进行排序，代码仍然可以工作，但可能会进行更多不必要的计算，
        # 因为没有利用排序来进行剪枝。这样做可能会影响性能，但结果集不会受到影响。
        # 为什么排序？
        # 优化和剪枝：
        # 排序后，可以在递归过程中尽早剪枝。因为一旦当前路径的和超过目标值 target，就可以停止进一步
        # 的搜索。
        # 例如，如果 candidates 是有序的，一旦添加的元素使当前路径的和超过 target，我们就可以直接
        # 返回，不必继续考虑后续的元素，因为它们只会使和更大。
        # 避免重复计算：
        # 排序还可以帮助避免重复计算。例如，如果 candidates 包含相同的元素或存在多种排列组合，排序
        # 可以确保我们以统一的顺序处理它们，减少冗余。
        candidates.sort()
        backtrack(0, [])
        return result
    
candidates = [2,3,6,7]
target = 7
solution = Solution()
print('Result1 = ', solution.combinationSum(candidates, target))
print('\n')

candidates = [2,3,5]
target = 8
print('Result2 = ', solution.combinationSum(candidates, target))
print('\n')

candidates = [2]
target = 1
print('Result3 = ', solution.combinationSum(candidates, target))