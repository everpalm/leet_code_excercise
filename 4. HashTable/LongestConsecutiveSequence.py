'''
Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

Use sets to optimize the runtime of your solution.

Input: An unsorted array of integers, nums.

Output: An integer representing the length of the longest consecutive sequence in nums.

Example:

Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.
'''
# WRITE LONGEST_CONSECUTIVE_SEQUENCE FUNCTION HERE #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
####################################################
def longest_consecutive_sequence(nums):
    # if len(nums) == 0:
    #     return 0
    # temp = sorted(nums)
    # sort = set()
    # sort.add(0)
    # prev = 0
    # for num in temp:
    #     prev = num - 1
    #     print('prev = ', prev)
    #     print('sort = ', sort)
    #     if prev not in sort:
    #         return len(sort) - 1
    #     sort.add(num)
    # print('sort = ', sort)
    
    if not nums:
        return 0

    # Convert the list to a set for O(1) lookups
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

            max_length = max(max_length, length)

    return max_length    

    # num_set = set(nums)
    # longest_sequence = 0
    
    # for num in nums:
    #     if num - 1 not in num_set:
    #         current_num = num
    #         current_sequence = 1
            
    #         while current_num + 1 in num_set:
    #             current_num += 1
    #             current_sequence += 1
            
    #         longest_sequence = max(longest_sequence, current_sequence)
    
    # return longest_sequence

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""