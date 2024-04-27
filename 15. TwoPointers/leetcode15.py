'''
15. 3Sum
Medium

Topics
Companies

Hint
Given an integer array nums, return all the triplets [nums[i], nums[j],
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k]
== 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not
matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
class Solution:
    def three_sum(self, nums: list) -> list:
        nums.sort()  # Sort the list first, O(n) = nlog(n)
        result = []
        n = len(nums)

        for i in range(n-2):
            print(f'i = {i}')
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, n-1
            print(f'left = {left}, right = {right}')
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Move left and right to the next different numbers to
                    # avoid duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return result

# Commenting out the function call
# nums = [-1, 0, 1, 2, -1, -4]
# print(three_sum(nums))

my_solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(f'Result1 = {my_solution.three_sum(nums)}')
