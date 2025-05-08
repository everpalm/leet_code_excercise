'''
268. Missing Number
Easy

Topics
Companies
Given an array nums containing n distinct numbers in the range [0, n], return
the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is
the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is
the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is
the missing number in the range since it does not appear in nums.

Constraints:
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
'''
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n + 1):
            found = False
            for num in nums:
                if i == num:
                    found = True
                    break
            if not found:
                return i
            
    def sumNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summary = int(n * (n + 1) / 2)
        total = sum(nums)
        return summary - total
    
    def optimized(self, nums: List[int]) -> int:
        n = len(nums)
        missing = 0
        for i in range(n + 1):
            missing ^= i
        
        for num in nums:
            missing ^= num

        return missing

if __name__ == '__main__':
    sol = Solution()
    nums = [3,0,1]
    print('Example 1 = ', sol.missingNumber(nums))  # Expected 2
    print('Example 1-1 = ', sol.sumNumber(nums))  # Expected 2
    print('Example 1-2 = ', sol.optimized(nums))  # Expected 2
    
    nums = [0,1]
    print('Example 2 = ', sol.missingNumber(nums))  # Expected 2
    print('Example 2-1 = ', sol.sumNumber(nums))  # Expected 2
    print('Example 2-2 = ', sol.optimized(nums))  # Expected 2
    
    nums = [9,6,4,2,3,5,7,0,1]
    print('Example 3 = ', sol.missingNumber(nums))  # Expected 8
    print('Example 3-1 = ', sol.sumNumber(nums))  # Expected 8
    print('Example 3-2 = ', sol.optimized(nums))  # Expected 8
