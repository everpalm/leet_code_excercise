'''
Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

Your function should take two arguments:
nums: a list of integers representing the input array
target: an integer representing the target sum

Your function should return a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum. If there is no such subarray, your function should return an empty list.

For example:

nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))  # should print [1, 3]

Note that there may be multiple subarrays that add up to the target sum, but your function only needs to return the indices of any one such subarray. Also, the input list may contain both positive and negative integers.
'''
# WRITE SUBARRAY_SUM FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################
def subarray_sum(nums, target):
    cumulative_sum = 0
    # subarray = {0: -1} # Why do we need this? The index refers to where the summary occurs
    subarray = {0: -1} # e.g. summary differnce 1 means it's from value 2 (key = 1) and value 1 (key = 0) 
    # subarray = {}
    # print('subarray = ', subarray)
    for key, value in enumerate(nums): # Iterate the list and save the summaries in an hash table
        # complement = target - cumulative_sum
        cumulative_sum += value
        residue = cumulative_sum - target
        # print('residue = ', residue)
        # print('subarray = ', subarray)
        if residue in subarray:
            # print('subarray[complement] = ', subarray[residue])
            return [subarray[residue] + 1, key]
        subarray[cumulative_sum] = key
    # sum_indices = {0: -1}  # Initialize with 0 sum at index -1 to handle cases where a subarray starts from index 0
    # cumulative_sum = 0

    # for i, num in enumerate(nums):
    #     cumulative_sum += num  # Update the cumulative sum

    #     # Check if cumulative_sum - target exists in sum_indices
    #     if (cumulative_sum - target) in sum_indices:
    #         # We found a subarray with the target sum
    #         return [sum_indices[cumulative_sum - target] + 1, i]

    #     # Add the current cumulative sum to sum_indices if not present
    #     if cumulative_sum not in sum_indices:
    #         sum_indices[cumulative_sum] = i

    # If no subarray with the target sum is found
    return []

nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""

