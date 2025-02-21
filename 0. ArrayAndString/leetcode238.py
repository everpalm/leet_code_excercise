'''
238. Product of Array Except Self
Medium

Topics
Companies

Hint
Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].
[1, 2, 3] --> [1, 2, 3, 6] --> [6]
[1, 2, 3, 4] --> [1, 2, 3, 4, 6, 8, 12, 24] --> [6, 8 , 12, 24]

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

 
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]


Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Note:
 1  [1] [2] [3]
[0]  1  [2] [3]
[0] [1]  1  [3]
[0] [1] [2]  1
^^^^^^^^^^ start out with the left side
answer[0] = 1
answer[1] = answer[0] * num[0] = 1 * 1
answer[2] = answer[1] * num[1] = 1 * 2
answer[3] = answer[2] * num[2] = 2 * 3
'''
# import operator


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        # The answer array to be returned
        answer = [0]*length
        print('answer = ', answer)
        # answer[i] contains the product of all the elements to the left
        # For the element at index 0, there are no elements to the left, so answer[0] should be 1
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
            print(f'answer[{i}] = ', answer[i])
        # print('answer = ', operator.mul(nums))
        # R is a running product of elements to the right
        multiplier = 1
        for j in reversed(range(length)):
            # For the index 'i', R would contain the product of all elements to the right. We update R accordingly
            # print('j = ', j)
            answer[j] = answer[j] * multiplier
            print(f'R answer[{j}] = ', answer[j])
            multiplier *= nums[j]
        return answer

        # Brute-force solution
        # result = []
        # Loop over each element in nums
        # for i in range(len(nums)):
        #     product = 1
        #     # Multiply all elements except itself
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     result.append(product)
        # return result
    

my_solution = Solution()
nums = [1, 2, 3, 4]
result = my_solution.productExceptSelf(nums)
print('Test1 result = ', result)

my_solution = Solution()
nums = [-1, -1, 0, -3, -3]
result = my_solution.productExceptSelf(nums)
print('Test2 result = ', result)