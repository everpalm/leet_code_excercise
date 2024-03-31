'''
Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).

Input:
A list of integers nums.

Output:
A list of integers representing the numbers in the input array nums that appear more than once. If no duplicates are found in the input array, return an empty list [].
'''
# WRITE FIND_DUPLICATES FUNCTION HERE #
#                                     #
#                                     #
#                                     #
#                                     #
#######################################
def find_duplicates(nums):
    # duplicates = []
    # my_list = {}
    # for index, value in enumerate(nums):
        # print('index = ', index)
        # print('value = ', value)
    # count = 0
    # for index, value in enumerate(nums):
    #     count += 1 
    #     my_list[value] =  count
    # print('my_list = ', my_list  )

    # for values in my_list.values():
    #     duplicates.append(values)
    # print('duplicates = ', duplicates)
    # return duplicates
    num_counts = {}
    print('nums = ', nums)
    for num in nums:
        temp = num_counts.get(num, 0)
        print('num = ', num)
        print('temp = ', temp)
        # num_counts[num] = num_counts.get(num, 0) + 1
        num_counts[num] = temp + 1
    print('num_counts = ', num_counts)
    duplicates = []
    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)
 
    return duplicates        
        



print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

