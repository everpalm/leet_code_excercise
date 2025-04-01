'''
Leetcode 485: Max Consecutive Ones

Leetcode: Easy
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''
class Solution(object):
    # def findMaxConsecutiveOnes(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     max_num = current_num = nums[0]
    #     for num in nums[1:]:
    #         if num == 1:
    #             current_num = max(num, current_num + num)
    #         else:
    #             current_num = num
    #         max_num = max(current_num, max_num)
    #     return max_num
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num == 1:
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 0
                
        # Final check to account for ending on a sequence of 1s
        max_count = max(max_count, current_count)
        
        return max_count
    
    def enumerateFindMaxConsecutiveOnes(self, nums):
        max_count = 0
        count = 0

        for i, num in enumerate(nums):
            count = count + 1 if num == 1 else 0
            max_count = max(max_count, count)

        return max_count



my_instance = Solution()
print('test = ', my_instance.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print('test = ', my_instance.findMaxConsecutiveOnes([0, 0, 0, 0, 0, 0]))
print('test = ', my_instance.findMaxConsecutiveOnes([1, 1, 1, 1, 1, 1]))
print('test = ', my_instance.findMaxConsecutiveOnes([]))


'''
Example 3:

    Input: nums = [1 1 1 1 1 1]
    Output: 6

    
Example 4:

    Input: nums = [0 0 0 0]
    Output: 0

'''