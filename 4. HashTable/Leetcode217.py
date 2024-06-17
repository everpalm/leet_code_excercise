'''
217. Contains Duplicate
Solved
Easy

Topics
Companies
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # my_hash = {}
        # count = 0
        # for num in nums:
        #     count = my_hash.get(num, 0)
        #     count += 1
        #     if count > 1:
        #         return True
        #     else:
        #         my_hash[num] = count
        # return False
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num) 
        return False

array1 = [1, 2, 3, 4]
print('test1 nums = ', array1)
my_solution = Solution()
print('result = ', my_solution.containsDuplicate(array1))

array2 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print('test2 nums = ', array2)
my_solution = Solution()
print('result = ', my_solution.containsDuplicate(array2))

array3 = [1, 2, 3, 1]
print('test3 nums = ', array3)
my_solution = Solution()
print('result = ', my_solution.containsDuplicate(array3))