'''344. Reverse String
Easy

Topics
Companies

Hint
Write a function that reverses a string. The input string is given as an array
of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 
Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
'''
from typing import List

class Solution(object):
    def reverseString(self, s: List) -> List[int]:
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
        # return s[::-1]


my_solution = Solution()
test_data = ['h', 'e', 'l', 'l', 'o']
print('Example 1 = ', my_solution.reverseString(test_data))

test_data = ["H","a","n","n","a","h"]
print('Example 2 = ', my_solution.reverseString(test_data))