'''
46. Permutations
Medium

Topics
Companies
Given an array nums of distinct integers, return all the possible permutations
. You can return the answer in any order.

 Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
 
Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''
#Path is nums = [1, 2, 3]
        #Path choose [1], leftpop then permute [2, 3] => [1, 2, 3], [1, 3, 2]
        #Path choose [2], leftpop then permute [3, 1] => [2, 3, 1], [2, 1, 3]
        #Path choose [3], leftpop then permute [1, 2] => [3, 1, 2], [3, 2, 1]
        #Back to permute [3]
        #Back to permute [2, 3] 
        #Choose [2] then [1] then [3]
        #Choose [2] then [3] then [1]
        #Choose [3] then [1] + [2]
        #Choose [3] then [2] + [1]
# import itertools

class Solution:
    def permute(self, nums):
#         # Generate all permutations using itertools.permutations
        # permutations = itertools.permutations(nums)
#         # Convert each permutation tuple to a list
#         result = [list(p) for p in permutations]
        result = []
        # Base case
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result

# Test cases
solution = Solution()
print(solution.permute([1, 2, 3]))  # Expected output: [[1,2,3], [1,3,2],
                                    # [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
print(solution.permute([0, 1]))     # Expected output: [[0,1], [1,0]]
print(solution.permute([1]))        # Expected output: [[1]]
