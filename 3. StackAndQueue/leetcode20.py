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
                stack.pop()  # Pop the matching opening bracket
            else: # Open bracket
                stack.append(char)  # Push opening bracket onto stack
        
        # If stack is empty, all brackets are matched correctly
        return not stack

    def is_valid_parentheses_brute_force(self, s):
        """
        暴力解法: 不断删除相邻的匹配括号对
        时间复杂度: O(n^2)\, 其中n是字符串长度
        空间复杂度: O(n)
        """
        while True:
            # 记录原始字符串长度
            original_length = len(s)
            
            # 替换所有匹配的括号对
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
            
            # 如果字符串长度没有变化，说明无法继续删除
            if len(s) == original_length:
                break
        
        # 如果最终字符串为空，说明所有括号都正确匹配
        return len(s) == 0

# my_solution = Solution()
# Example calls to test the function (commented out)
# print(my_solution.is_valid_parentheses("()"))         # Output: True
# print(my_solution.is_valid_parentheses("()[]{}"))     # Output: True
# print(my_solution.is_valid_parentheses("(]"))         # Output: False
# print(my_solution.is_valid_parentheses("([)]"))       # Output: False
# print(my_solution.is_valid_parentheses("{[()]}"))       # Output: True
# print(my_solution.is_valid_parentheses(""))       # Output: True
# print(my_solution.is_valid_parentheses("abcd"))       # Output: True

solution = Solution()
print(solution.is_valid_parentheses_brute_force("()[]{}"))  # 应该返回 True
print(solution.is_valid_parentheses_brute_force("([)]"))    # 应该返回 False
print(solution.is_valid_parentheses_brute_force("()"))    # 应该返回 True