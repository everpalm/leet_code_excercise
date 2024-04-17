'''
49. Group Anagrams
Solved
Medium

Topics
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

You have been given an array of strings, where each string may contain only
lowercase English letters. You need to write a function group_anagrams
(strings) that groups the anagrams in the array together using a hash table
(dictionary). The function should return a list of lists, where each inner
list contains a group of anagrams.

For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"],
the function should return [["eat","tea","ate"],["tan","nat"],["bat"]] because
the first three strings are anagrams of each other, the next two strings are
anagrams of each other, and the last string has no anagrams in the input array.

You need to implement the group_anagrams(strings) function and return a list
of lists, where each inner list contains a group of anagrams according to the
above requirements.
'''
# WRITE GROUP_ANAGRAMS FUNCTION HERE #
#                                    #
#                                    #
#                                    #
#                                    #
######################################
def group_anagrams(strings):
    print('strings = ', strings)
    anagram_dict = {}

    for s in strings:
        # Sort the string and use it as a key
        # key = tuple(sorted(s))
        key = str(sorted(s))
        # If the key exists, append the string to the corresponding list
        if key in anagram_dict:
            anagram_dict[key].append(s)
        # If the key doesn't exist, create a new entry with the string in a new list
        else:
            anagram_dict[key] = [s]

    # Return the values of the dictionary as a list of lists
    return list(anagram_dict.values())
    # buffers = []
    # replicates = []
    # non_replica = []
    # for string in strings:
    #     count = 0
    #     anagrams = {}
    #     for char in string:
    #         count = anagrams.get(char, 0)
    #         anagrams[char] = count + 1
    #     # print ('anagrams = ', anagrams)
        
    #     if anagrams not in buffers:
    #         buffers.append(anagrams)
    #         print('buffers =', buffers)
            
        # if string in buffers:
        # if string in buffers:
        #     replicates.append(string)
        #     print('replicates =', replicates )
        # else:
        #     non_replica.append(string)
        #     print('non_replica =', non_replica )
    # return replicates.append(non_replica)
    



print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )

print("\n4th set:")
print( group_anagrams([]) )

print("\n5th set:")
print( group_anagrams(["aaa", "aaa", "aaa"]))

print("\n6th set:")
print( group_anagrams(["aaa", "aaa", "aaa", "bbb", "bbb"]))

"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""