'''
53. Maximum Subarray
Medium

Classic!

Topics
Companies
Given an integer array nums, find the subarray with the largest sum, and
return its sum.

Example 1:
input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
 
Follow up: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle.
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    # Return 0 if input list is empty
        if not nums:
            return 0
    
        # Initialize max_sum and current_sum
        max_sum = current_sum = nums[0]
    
        # Iterate through the remaining elements
        for num in nums[1:]:
            # Update current_sum
            current_sum = max(num, current_sum + num)
            # max_sum = max(max_sum, current_sum)
            if current_sum > max_sum:
                max_sum = current_sum
    
        # Return the maximum subarray sum
        return max_sum
    
    def boute_force(self, nums: List[int]) -> int:
        current_sum = max_sum = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum > max_sum:
                    max_sum = current_sum
        return max_sum
    

solution = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Result1 = ", solution.maxSubArray(nums))
print("Result1-1 = ", solution.boute_force(nums))

nums = [1]
print("Result2 = ", solution.maxSubArray(nums))
print("Result2-1 = ", solution.boute_force(nums))

nums = [5,4,-1,7,8]
print("Result3 = ", solution.maxSubArray(nums))
print("Result3-1 = ", solution.boute_force(nums))


