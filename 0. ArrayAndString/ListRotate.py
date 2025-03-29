'''
Coding Exercise 105
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

'''
This rotate function is designed to rotate the elements of a list nums to the right by k positions. Let's break down what each part of the function does:
Function Definition:
def rotate(nums, k):
This line defines a function named rotate that takes two parameters:
nums: a list of numbers.
k: the number of positions by which the elements in the list should be rotated.
Modulo Operation for Rotation Count:
k = k % len(nums)
This line adjusts the value of k to ensure it is within the bounds of the list's length. It uses the modulo operator %. The modulo operation here serves two purposes:
If k is greater than the length of nums, it wraps k around. For example, if the list has 5 elements and k is 6, this operation will turn k into 1, as rotating a list of 5 elements by 6 steps is the same as rotating by 1 step.
If k is negative or zero, it effectively handles these cases by converting k into a valid positive index.
List Rotation Using Slicing:
nums[:] = nums[-k:] + nums[:-k]
This line performs the actual rotation of the list:
nums[-k:]: This slice gets the last k elements of the list. In Python, negative indices are used to count from the end of the list backwards, so -k refers to the k-th element from the end.
nums[:-k]: This slice gets all the elements of the list except for the last k elements. The :-k slice means "start from the beginning of the list and go up to, but not including, the k-th element from the end."
The + operator concatenates these two slices, effectively placing the last k elements at the beginning and the rest of the elements after them.
nums[:] =: This syntax is used to update the contents of nums in place with the new order of elements. It ensures that the original list referred to by nums is modified, rather than creating a new list.
In summary, the rotate function takes a list and an integer k, and rotates the list to the right by k positions. This means that each element is shifted k positions to the right, and the elements that overflow from the end of the list are wrapped around to the front.
'''
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