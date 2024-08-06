'''
20. Valid Parentheses
Attempted
Easy

Topics
Companies

Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
,determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
class Solution(object):
    def is_valid_parentheses(self, s):
        # Dictionary to match the corresponding brackets (A list of close brackets)
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Stack to keep track of opening brackets
        stack = []
        
        for char in s:
            if char in bracket_map: # Close bracket
                # If the stack is empty or the top of the stack does not match the closing bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                print('pop stack = ', stack)
                stack.pop()  # Pop the matching opening bracket
            else: # Open bracket
                stack.append(char)  # Push opening bracket onto stack
                print('append stack = ', stack)
        
        # If stack is empty, all brackets are matched correctly
        return not stack

my_solution = Solution()
# Example calls to test the function (commented out)
print(my_solution.is_valid_parentheses("()"))         # Output: True
print(my_solution.is_valid_parentheses("()[]{}"))     # Output: True
print(my_solution.is_valid_parentheses("(]"))         # Output: False
print(my_solution.is_valid_parentheses("([)]"))       # Output: False
print(my_solution.is_valid_parentheses("{[()]}"))       # Output: True
print(my_solution.is_valid_parentheses(""))       # Output: True
# print(my_solution.is_valid_parentheses("abcd"))       # Output: True