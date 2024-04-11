'''
You are given a list of n integers and a non-negative integer k.

Your task is to write a function called rotate that takes the list of integers and an integer k as input and rotates the list to the right by k steps.

The function should modify the input list in-place, and you should not return anything.

Constraints:
Each element of the input list is an integer.
The integer k is non-negative.

Function signature: def rotate(nums, k):

Example:
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Function call: rotate(nums, k)
Output: nums = [5, 6, 7, 1, 2, 3, 4]

Explanation: The list has been rotated to the right by 3 steps:

[7, 1, 2, 3, 4, 5, 6]
[6, 7, 1, 2, 3, 4, 5]
[5, 6, 7, 1, 2, 3, 4]
'''
# WRITE ROTATE FUNCTION HERE #
#                            #
#                            #
#                            #
#                            #
##############################
# def rotate(nums, k):
#     if k > len(nums):
#         return nums
#     if k == 0:
#         return nums
#     counter = 0
#     for num in nums:
#         if counter < k+1:
#             nums.append(nums.pop(0))
#             counter+=1
def rotate(nums, k):
    # Calculate the effective rotation.
    # The modulo operator (%) is used to handle cases where
    # k is larger than the length of the list. This ensures
    # that the rotation count is within the bounds of the list's length.
    k = k % len(nums)
    print('k = ', k)
    # nums[:] = nums[-k:] + nums[:-k]
    # This line performs the rotation of the list.
    # Let's break down the slicing operations:
 
    # nums[-k:]:
    # This slice gets the last 'k' elements of the list.
    # In Python, negative indices start counting from the end of the list.
    # So, -k is the k-th element from the end.
    # For example, if k is 2, nums[-2:] gets the last two elements.
 
    # nums[:-k]:
    # This slice gets all elements of the list except the last 'k'.
    # Here, -k as the stop index in slicing means to stop before
    # the k-th element from the end.
    # For example, if k is 2, nums[:-2] gets all elements except the last two.
 
    # nums[-k:] + nums[:-k]:
    # This concatenates the last 'k' elements (nums[-k:])
    # with the first part of the list (nums[:-k]),
    # effectively rotating the list.
 
    # nums[:] = ...
    # Finally, nums[:] = is used to update the list in place.
    # It changes the original list 'nums' to be the rotated version.
    # Without [:], a new list would be created, and the original list
    # would remain unchanged.
    nums[:] = nums[-k:] + nums[:-k]
    
nums = [1, 2, 3, 4, 5, 6, 7]
k = 8
rotate(nums, k)
print("Rotated array:", nums)

k = 7
rotate(nums, k)
print("Rotated array:", nums)

k = 0
rotate(nums, k)
print("Rotated array:", nums)

# k = -1
# rotate(nums, k)
# print("Rotated array:", nums)

# nums = []
# k = 2
# rotate(nums, k)
# print("Rotated array:", nums)

"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""