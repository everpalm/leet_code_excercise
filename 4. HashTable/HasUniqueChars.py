'''
Write a function called has_unique_chars that takes a string as input and
returns True if all the characters in the string are unique, and False
otherwise.

For example, has_unique_chars('abcdefg') should return True, while
has_unique_chars('hello') should return False.
'''
# WRITE HAS_UNIQUE_CHARS FUNCTION HERE #
#                                      #
#                                      #
#                                      #
#                                      #
########################################
def has_unique_chars(input_string):
    # temp = {}
    # for char in input_string:
    #     temp[char] = True
    # my_set = set(temp)
    # print('result = ', my_set.intersection(my_set) == my_set)
    seen_chars = set()
    for char in input_string:
        # If char is already in seen_chars, it's not unique
        if char in seen_chars:
            return False
        # Add char to seen_chars
        seen_chars.add(char)
    # If loop completes, all chars were unique
    return True

print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""