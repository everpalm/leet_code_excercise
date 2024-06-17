'''
167. Two Sum II - Input Array Is Sorted
Medium

Topics
Companies
Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an
integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not
use the same element twice.

Your solution must use only constant extra space.


Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We 
return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We 
return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We
return [1, 2].
 

Constraints:
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
'''
class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        # complement_list = {}
        # # answer = []
        # for key, value in enumerate(numbers):
        #     # print(f'key = {key}, value = {value}')
        #     complement = target - value
        #     if complement in complement_list:
        #         # print(f'complement = {complement}')
        #         return [complement_list[complement], key]
        #     complement_list[value] = key
        #     # print(f'complement_list = {complement_list}')
        # return []

        index1, index2 = 0, len(numbers) - 1  # 0-indexed pointers

        while index1 < index2:
            current_sum = numbers[index1] + numbers[index2]
            if current_sum == target:
                return [index1 + 1, index2 + 1]  # return 1-indexed positions
            elif current_sum < target:
                index1 += 1
            else:
                index2 -= 1

# Example test cases (commented out)
# print(two_sum_sorted([2, 7, 11, 15], 9))  # Output: [1, 2]
# print(two_sum_sorted([2, 3, 4], 6))        # Output: [1, 3]
# print(two_sum_sorted([-1, 0], -1))         # Output: [1, 2]


my_solution = Solution()

numbers = []
target = 9
print(f'Result0 = {my_solution.twoSum(numbers, target)}')

numbers = [2,7,11,15]
target = 9
print(f'Result1 = {my_solution.twoSum(numbers, target)}')

numbers = [2,3,4]
target = 6
print(f'Result2 = {my_solution.twoSum(numbers, target)}')

numbers = [-1,0]
target = -1
print(f'Smarllest Result = {my_solution.twoSum(numbers, target)}')

large_test_array = list(range(1, 3*104+1))  # Array from 1 to 3 * 104
large_test_target = 311 + 312  # Last two elements sum
print(f'Largest Result = {my_solution.twoSum(large_test_array, large_test_target)}')

large_test_array = list(range(1, 3*52+1))  # Array from 1 to 3 * 52
large_test_target = 155 + 156  # Last two elements sum
print(f'Middle Result = {my_solution.twoSum(large_test_array, large_test_target)}')

np_array = [-1000, -500, 500, 1000] # Array from 1 to 3 * 52
np_target = 0  # Last two elements sum
print(f'Negtive and Positive Result = {my_solution.twoSum(np_array, np_target)}')