'''
90. Subsets II
Medium

Topics
Companies
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in
any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''
class Solution:
    def subsetsWithDup(self, nums):
        def backtrack(start, path):
            # Add the current path to the result
            result.append(path)
            # Explore further subsets
            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i-1]:
                    continue
                # Recurse with the current number included
                backtrack(i + 1, path + [nums[i]])

        nums.sort()  # Sort the numbers to handle duplicates
        result = []
        backtrack(0, [])
        return result

# Test the function with the given examples
solution = Solution()
print(solution.subsetsWithDup([1, 2, 2]))  # Expected: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
print(solution.subsetsWithDup([0]))        # Expected: [[], [0]]

