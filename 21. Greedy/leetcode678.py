'''
678. Valid Parenthesis String
Medium

Topics
Companies

Hint
Given a string s containing only three types of characters: '(', ')' and '*',
return true if s is valid.

The following rules define a valid string:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left
parenthesis '(' or an empty string "".
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true
 
Constraints:
1 <= s.length <= 100
s[i] is '(', ')' or '*'.
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        open_min = 0  # Minimum number of open parentheses
        open_max = 0  # Maximum number of open parentheses
        
        for char in s:
            if char == '(':
                open_min += 1
                open_max += 1
            elif char == ')':
                open_min -= 1
                open_max -= 1
            elif char == '*':
                open_max += 1
                open_min -= 1
            
            if open_min < 0:
                open_min = 0
            
            if open_max < 0:
                return False
        
        return open_min == 0

# Example usage
sol = Solution()
print(sol.checkValidString("()"))    # Output: True
print(sol.checkValidString("(*)"))   # Output: True
print(sol.checkValidString("(*))"))  # Output: True
print(sol.checkValidString(""))  # Output: True
print(sol.checkValidString("("))  # Output: False
print(sol.checkValidString(")"))  # Output: False
print(sol.checkValidString("*"))  # Output: True
