'''
Coding Exercise 106
Given an array of integers nums, write a function max_subarray(nums) that finds the contiguous subarray (containing at least one number) with the largest sum and returns its sum.

Remember to also account for an array with 0 items.

Function Signature:
def max_subarray(nums):

Input:
A list of integers nums.

Output:
An integer representing the sum of the contiguous subarray with the largest sum.

Example:
max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
Output: 6
'''
# WRITE THE MAX_SUBARRAY FUNCTION HERE #
#                                      #
#                                      #
#                                      #
#                                      #
########################################
# def max_subarray(nums):
#     if not nums:
#         return 0
#     max_sum = 0
#     # current_max = 0
#     for i in range(len(nums)):
#         my_sum = nums[i]
#         # current_max = max(my_sum, current_max)
#         for j in range(i+1, len(nums)):
#             my_sum = my_sum + nums[j]
#             max_sum = max(max_sum, my_sum)
#     #         print('i = ', i)
#     #         print('j = ', j)
#     #         print('my_sum = ', my_sum)
#     #         print('max_sum = ', max_sum)
#     return max_sum
# def max_subarray(nums):
#     # Edge case: if nums is empty
#     if not nums:
#         return 0

#     max_so_far = current_max = nums[0]
#     for num in nums[1:]:
#         # Update current_max either by adding the current num or starting new from current num
#         current_max = max(num, current_max + num)
#         # Update max_so_far to ensure it holds the maximum sum encountered so far
#         max_so_far = max(max_so_far, current_max)
    
#     return max_so_far

# Uncomment the line below to test the function
# print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
'''
Explanation: The contiguous subarray [4, -1, 2, 1] has the largest sum, which is 6.

This code implements the Kadane's algorithm to find the maximum subarray sum. Let's go through the code and understand the logic step by step:

if not nums: return 0: This line checks if the input list nums is empty. If it's empty, the function returns 0, as there's no subarray to calculate the sum.
max_sum = current_sum = nums[0]: Both max_sum and current_sum are initialized to the first element of the input list nums. max_sum stores the maximum subarray sum found so far, while current_sum keeps track of the maximum subarray sum ending at the current position.
for num in nums[1:]:: The loop iterates through the remaining elements of the input list nums, starting from the second element.
current_sum = max(num, current_sum + num): For each element num in the loop, this line updates the current_sum by taking the maximum of two values: the current element itself (num) and the sum of the current element and the previous current_sum. This step ensures that if the previous current_sum is negative, it's better to start a new subarray from the current element (since adding a negative value to the current element would only decrease the sum).
max_sum = max(max_sum, current_sum): After updating the current_sum, this line compares it with the current max_sum. If the current_sum is greater than the max_sum, it updates the max_sum value to be the current_sum. This way, the max_sum variable always holds the maximum subarray sum found so far.
return max_sum: After iterating through all the elements in the input list, the function returns the final value of max_sum, which represents the sum of the contiguous subarray with the largest sum.

By using the Kadane's algorithm, this code efficiently finds the maximum subarray sum with a linear time complexity of O(n), where n is the length of the input list nums.
'''
def max_subarray(nums):
    # Return 0 if input list is empty
    if not nums:
        return 0
 
    # Initialize max_sum and current_sum
    max_sum = current_sum = nums[0]
 
    # Iterate through the remaining elements
    for num in nums[1:]:
        # Update current_sum
        current_sum = max(num, current_sum + num)
        # print('current_sum = ', current_sum)
        # Update max_sum if current_sum is larger
        max_sum = max(max_sum, current_sum)
        # print('max_sum = ', max_sum)
 
    # Return the maximum subarray sum
    return max_sum
# Example 1: Simple case with positive and negative numbers
input_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_1 = max_subarray(input_case_1)
print("Example 1: Input:", input_case_1, "\nResult:", result_1)  

# Example 2: Case with a negative number in the middle
input_case_2 = [1, 2, 3, -4, 5, 6]
result_2 = max_subarray(input_case_2)
print("Example 2: Input:", input_case_2, "\nResult:", result_2) 

# Example 3: Case with all negative numbers
input_case_3 = [-1, -2, -3, -4, -5]
result_3 = max_subarray(input_case_3)
print("Example 3: Input:", input_case_3, "\nResult:", result_3) 


"""
    EXPECTED OUTPUT:
    ----------------
    Example 1: Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
    Result: 6
    Example 2: Input: [1, 2, 3, -4, 5, 6] 
    Result: 13
    Example 3: Input: [-1, -2, -3, -4, -5] 
    Result: -1
    
"""
