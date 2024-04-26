'''
242. Valid Anagram
Solved
Easy

Topics
Companies
Given two strings s and t, return true if t is an anagram of s, and false
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.

 
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt
your solution to such a case?
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        
        char_count = {}
        
        # Count frequency of each character in s
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
                
        # Decrease count for each character found in t
        for char in t:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] < 0:
                    return False
            else:
                return False
        
        # If all counts zero, they are anagrams
        for count in char_count.values():
            if count != 0:
                return False
            
        return True

# Uncomment to test the function with example inputs
# print(is_anagram("anagram", "nagaram"))  # Should return True
# print(is_anagram("rat", "car"))  # Should return False

    
my_solution = Solution()

s = "anagram"
t = "nagaram"
print('s = ', s)
print('t = ', t)
print('Expected = ', True)
print('Output = ', my_solution.isAnagram(s, t))

s = "rat"
t = "car"
print('s = ', s)
print('t = ', t)
print('Expected = ', True)
print('Output = ', my_solution.isAnagram(s, t))