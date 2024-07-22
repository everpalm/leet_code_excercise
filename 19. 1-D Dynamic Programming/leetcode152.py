'''
152. Maximum Product Subarray
Medium

Topics
Companies
Given an integer array nums, find a subarray that has the largest product,
and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 
Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
integer.
'''
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
# if not nums:
        #     return 
        # n = len(nums)
        # #dp = [0]* (n+1)
        # prev2 = 1
        # prev1 = nums[0]
        # max_product = 0
        # for i in range(1, n):
        #     current = prev2 * prev1
        #     max_product = max(current, max_product)
        #     prev1, prev2 = prev2, current
        # return max_product
        if not nums:
            return 0

        max_product = min_product = result = nums[0]

        for num in nums[1:]:
            temp_max = max(num, max_product * num, min_product * num)
            min_product = min(num, max_product * num, min_product * num)
            max_product = temp_max
            result = max(result, max_product)

        return result
    

solution = Solution()
nums = [2,3,-2,4]
print('Result1 = ', solution.maxProduct(nums))
nums = [-2,0,-1]
print('Result2 = ', solution.maxProduct(nums))
