'''
416. Partition Equal Subset Sum
Medium

Topics
Companies
Given an integer array nums, return true if you can partition the array into
two subsets such that the sum of the elements in both subsets is equal or
false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 
Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
'''
def canPartition(nums):
    total_sum = sum(nums)
    
    # If the total sum is odd, we cannot partition it into two equal subsets
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True  # We can always form a subset with sum 0 (empty subset)
    
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target]

# Example usage:
nums1 = [1, 5, 11, 5]
nums2 = [1, 2, 3, 5]

print(canPartition(nums1))  # Output: True
# print(canPartition(nums2))  # Output: False
