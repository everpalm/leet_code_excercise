'''
125. Valid Palindrome
Easy

Topics
Companies
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward. Alphanumeric characters include letters and
numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric
characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''
# import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # print(f's = {s}')
        normalized = ''.join([char.lower() for char in s if char.isalnum()])
        # print(f'normalized = {normalized}')
        return normalized == normalized[::-1]
        # converted_string = s.lower().replace(",", "").replace(":", "").replace(" ", "")
        # converted_string = re.sub(r'[A-Z0-9]', '', s.lower().replace(" ", ""))
        # print('converted_string = ', converted_string)
        # print('length = ', len(converted_string))
        # my_stack = []
        # for char in converted_string:
        #     my_stack.append(char)
        
        # for char in converted_string:
        #     if my_stack.pop() != char:
        #         return False
        # return True
        # for i in range(len(converted_string)):
    

my_solution = Solution()
s = "A man, a plan, a canal: Panama"
print('Expected Result1 = True. Output = ', my_solution.isPalindrome(s))

s = "race a car"
print('Expected Result2 = False. Output = ', my_solution.isPalindrome(s))

s = " "
print('Expected Result3 = True. Output = ', my_solution.isPalindrome(s))