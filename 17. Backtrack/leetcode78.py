'''
78. Subsets
Medium

Topics
Companies
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution i
any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''
from typing import List


class Solution():
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_length = len(nums)
        print('nums_length = ', nums_length)

        def backtrack(start, path):
            # 將當前部分解添加到結果集中
            print('start = ', start)
            print('path = ', path)
            result.append(path)
            # result.append(path[:])
            print('result = ', result)
            for i in range(start, nums_length):
                # 選擇nums[i]
                print('i = ', i)
                backtrack(i + 1, path + [nums[i]])
                # Append method add an element in-place
                # If I append to the path here, path in the result will change
                # path.append(nums[i])
                # backtrack(i + 1, path)
    
        result = []
        backtrack(0, [])
        return result
    
    def breakdown(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [lst + [num] for lst in result]
        return result

    def choices(self, nums: List[int], k: int) -> List[List[int]]:
        def backtrack(start: int, path: List[int]):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                # backtrack(i + 1, path + [nums[i]])
                backtrack(i + 1, path)
                path.pop()
    
        result = []
        backtrack(0, [])
        return result

nums = [1, 2, 3]
solution = Solution()
# print('Result1 = ', solution.subsets(nums))
# print('Result1-1 = ', solution.breakdown(nums))
# print('Result1-2 = ', solution.choices(nums, 1))
print('Result1-2 = ', solution.choices(nums, 2))
# print('Result1-2 = ', solution.choices(nums, 3))
print('\n')

nums = [0]
# print('Result2 = ', solution.subsets(nums))
# print('Result2-1 = ', solution.breakdown(nums))
# print('Result2-2 = ', solution.choices(nums, 1))
# print('Result2-2 = ', solution.choices(nums, 2))
# print('Result2-2 = ', solution.choices(nums, 3))