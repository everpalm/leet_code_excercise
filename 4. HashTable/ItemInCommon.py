'''
Write a function item_in_common(list1, list2) that takes two lists as input
and returns True if there is at least one common item between the two lists, 
False otherwise.
Use a dictionary to solve the problem that creates an O(n) time complexity.
'''
# WRITE ITEM_IN_COMMON FUNCTION HERE #
#                                    #
#                                    #
#                                    #
#                                    #
######################################
def item_in_common(list1, list2):
    # print('len(list1) = ', len(list1))
    # print('len(list2) = ', len(list2))
    # for i in range(len(list1)):
    #     print('list1 = ', list1[i])
    #     for j in range(len(list2)):
    #         print('list2 = ', list2[j])
    #         # return list1[i] == list2[j]
    #         if list1[i] == list2[j]:
    #             return True
    # return False
    my_dict = {}
    for i in list1:
        # print('i = ', i)
        my_dict[i] = True
        # print('my_dict[i] = ', my_dict[i])
 
    for j in list2:
        if j in my_dict:
            # print('j = ', j)
            # print('my_dict[j] = ', my_dict[j])
            return my_dict[j]
            #return True
    return False


list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""
