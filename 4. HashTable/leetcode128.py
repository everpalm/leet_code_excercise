'''
128. Longest Consecutive Sequence
Medium

Topics
Companies
Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_length = 0
        print('num_set = ', num_set)

        for num in num_set:
        # Check if it's the start of a sequence
            if num - 1 not in num_set:
                length = 1
                current_num = num
                print('current_num = ', current_num)
                print('num = ', num)
                # Count the length of the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    length += 1
                # Compare max length with current max length
                max_length = max(max_length, length)
        return max_length   



data = [100, 4, 200, 1, 3, 2]
my_solution = Solution()
print(my_solution.longestConsecutive(data))

data = [0, 1, 2, 3 ,4]
my_solution = Solution()
print(my_solution.longestConsecutive(data))

data = [4, 3, 2, 1, 0]
my_solution = Solution()
print(my_solution.longestConsecutive(data))

data = []
my_solution = Solution()
print(my_solution.longestConsecutive(data))

data = [1, 1, 1, 1, 1]
my_solution = Solution()
print(my_solution.longestConsecutive(data))
