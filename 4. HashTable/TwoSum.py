'''
Problem:
Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.

The main challenge here is to implement this function in one pass through the array. This means you should not iterate over the array more than once. Therefore, your solution should have a time complexity of O(n), where n is the number of elements in nums.

Input:
A list of integers nums .
A target integer target.

Output:
A list of two integers representing the indices of the two numbers in the input array nums that add up to the target. If no two numbers in the input array add up to the target, return an empty list [].
'''
# WRITE TWO_SUM FUNCTION HERE #
#                             #
#                             #
#                             #
#                             #
###############################
def two_sum(nums, target):
    buffer = {}
    for key, value in enumerate(nums): # Create an hash table with key iteration in nums
        # print('key = ', key)
        # print('value = ', value)
        complement = target - value
        # print('complement = ', complement)
        if complement in buffer: # Find complement in the hash table
            # print('Answer = ', [buffer[complement], key])
            return [buffer[complement], key]
        buffer[value] = key
        # print('buffer = ', buffer)
    return [] # the instruction request to return an empty list if no condition meets 
    
    
    
print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 4]
    [1, 3]
    [0, 3]
    [1, 3]
    []
    [2, 3]
    [0, 1]
    []

"""


