''''
You have been given a string of lowercase letters.

Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return None.

For example, if the input string is "leetcode", the function should return "l" because "l" is the first character that appears only once in the string. Similarly, if the input string is "hello", the function should return "h" because "h" is the first non-repeating character in the string.
'''
# WRITE THE FUNCTION HERE #
#                         #
#                         #
#                         #
#                         #
###########################
def first_non_repeating_char(string):
    duplicates = {}
    if string == '':
        return None
    for char in string:
        count = duplicates.get(char, 0)
        duplicates[char] = count + 1
    print('duplicates = ', duplicates)
    # for key, value in duplicates.items():
    #     print('key = ', key)
    #     print('value = ', value)
    #     if value == 1:
    #         break
    #     else:
    #         return None
    # return key
    for char in string:
        if duplicates[char] == 1:
            return char
    return None
print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )

print( first_non_repeating_char('abcde') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""