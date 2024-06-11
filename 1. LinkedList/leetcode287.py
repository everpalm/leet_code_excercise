'''
287. Find the Duplicate Number
Medium

Topics
Companies
Given an array of integers nums containing n + 1 integers where each integer
is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only
constant extra space.

 
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]   
Output: 3
 
Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer
which appears two or more times.
'''
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # num_count = {}
        # for num in nums:
        #     count = num_count.get(num, 0)
        #     num_count[num] = count + 1
        #     if count > 0:
        #         return num
        # Initialize the tortoise and hare
        tortoise = nums[0]
        hare = nums[0]
        
        # First phase: finding the intersection point
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                # print('tortoise = ', tortoise)
                break
        
        # Second phase: finding the entrance to the cycle
        tortoise = nums[0]
        # print('tortoise1 = ', tortoise)
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
            # print('tortoise2 = ', tortoise)
        # return hare
        return tortoise

    
my_solution = Solution()
nums = [1, 3, 4, 2, 2]
print('Result1 = ', my_solution.findDuplicate(nums))

nums = [3, 1, 3, 4, 2]
print('Result2 = ', my_solution.findDuplicate(nums))

nums = [3, 3, 3, 3, 3]
print('Result3 = ', my_solution.findDuplicate(nums))